"""
data_cleaning.py
Data cleaning and preprocessing for hotel bookings dataset
"""

import pandas as pd
import os

def load_data(path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)

def clean_data(df):
    """Perform basic cleaning on the DataFrame."""
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    # Fill missing 'agent' entries with 'Unknown'
    if 'agent' in df.columns:
        df['agent'] = df['agent'].fillna('Unknown')

    # Convert date columns to datetime
    date_cols = ['reservation_status_date', 'arrival_date']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Filter out negative ADR values
    if 'adr' in df.columns:
        df = df[df['adr'] >= 0]

    return df

def save_data(df, path):
    """Save the cleaned DataFrame to a CSV file."""
    df.to_csv(path, index=False)
    print(f'Cleaned data saved to: {path}')

def main():
    base_dir = os.path.dirname(__file__)
    raw_path = os.path.join(base_dir, '..', '01_Raw_Data', 'kaggle_hotel_booking.csv')
    clean_path = os.path.join(base_dir, '..', '01_Raw_Data', 'hotel_booking_clean.csv')

    print(f'Loading raw data from: {raw_path}')
    df = load_data(raw_path)

    print('Cleaning data...')
    df_clean = clean_data(df)

    print(f'Saving cleaned data to: {clean_path}')
    save_data(df_clean, clean_path)

if __name__ == '__main__':
    main()
