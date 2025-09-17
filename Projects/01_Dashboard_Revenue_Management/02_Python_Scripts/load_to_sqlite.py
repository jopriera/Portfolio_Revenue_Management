"""
load_to_sqlite.py
Load real and synthetic hotel booking CSVs into SQLite using pandas, with error handling and relative paths.
"""

import pandas as pd
import sqlite3
import os
import sys

# Build relative paths to data and database
base_dir = os.path.dirname(__file__)
real_csv = os.path.join(base_dir, '..', '01_Raw_Data', 'kaggle_hotel_booking.csv')
synth_csv = os.path.join(base_dir, '..', '01_Raw_Data', 'synthetic_data', 'synthetic_hotel_bookings.csv')
db_path   = os.path.join(base_dir, '..', 'portfolio.db')

def read_csv(path, name):
    try:
        print(f'Reading {name} data from: {path}')
        df = pd.read_csv(path)
        print(f'Success: {len(df)} rows loaded from {name}')
        return df
    except FileNotFoundError:
        print(f'ERROR: {name} file not found at {path}')
        sys.exit(1)
    except Exception as e:
        print(f'ERROR reading {name}: {e}')
        sys.exit(1)

def write_to_sql(df, table_name, conn):
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f'Success: table "{table_name}" written to database')
    except Exception as e:
        print(f'ERROR writing table {table_name}: {e}')
        sys.exit(1)

if __name__ == '__main__':
    # 1. Read the CSV files
    df_real  = read_csv(real_csv,  'Real bookings')
    df_synth = read_csv(synth_csv, 'Synthetic bookings')

    # 2. Connect to SQLite (creates portfolio.db if it doesn’t exist)
    try:
        print(f'Connecting to SQLite database at: {db_path}')
        conn = sqlite3.connect(db_path)
    except Exception as e:
        print(f'ERROR connecting to database: {e}')
        sys.exit(1)

    # 3. Write DataFrames to SQL tables
    write_to_sql(df_real,  'hotel_bookings',   conn)
    write_to_sql(df_synth, 'synthetic_bookings', conn)

    # 4. Close the connection
    conn.close()
    print('All tables loaded successfully. Database connection closed.')
