"""
data_cleaning.py
Funciones de limpieza y preprocesamiento de datos para Hotel Bookings.
"""

import pandas as pd
import os

def load_data(path):
    """Carga un CSV y retorna DataFrame."""
    return pd.read_csv(path)

def clean_data(df):
    """Aplica limpieza básica al DataFrame."""
    # 1. Eliminar duplicados
    df = df.drop_duplicates()
    
    # 2. Manejar valores faltantes
    # Ejemplo: rellenar nulos en 'agent' con 'Unknown'
    if 'agent' in df.columns:
        df['agent'] = df['agent'].fillna('Unknown')
    
    # 3. Conversión de tipos
    # Ejemplo: convertir columnas de fecha a datetime
    date_cols = ['reservation_status_date', 'arrival_date']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # 4. Filtrar valores atípicos de ADR (ejemplo)
    if 'adr' in df.columns:
        df = df[df['adr'] >= 0]
    
    return df

def save_data(df, path):
    """Guarda DataFrame limpio en CSV."""
    df.to_csv(path, index=False)
    print(f'Clean data saved to {path}')

def main():
    base_dir = os.path.dirname(__file__)
    raw_path   = os.path.join(base_dir, '..', '01_Raw_Data', 'kaggle_hotel_booking.csv')
    clean_path = os.path.join(base_dir, '..', '01_Raw_Data', 'hotel_booking_clean.csv')
    
    print(f'Loading raw data from {raw_path}')
    df = load_data(raw_path)
    
    print('Cleaning data...')
    df_clean = clean_data(df)
    
    print(f'Saving cleaned data to {clean_path}')
    save_data(df_clean, clean_path)

if __name__ == '__main__':
    main()
