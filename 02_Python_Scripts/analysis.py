"""
analysis.py
Exploratory Data Analysis for Hotel Bookings.
"""

import pandas as pd
import os

def load_data(path):
    """Carga un CSV y retorna un DataFrame."""
    return pd.read_csv(path)

def summary(df):
    """Imprime estadísticas descriptivas básicas."""
    print("=== Descriptive Statistics ===")
    print(df.describe(include='all'))

def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, '..', '01_Raw_Data', 'kaggle_hotel_booking.csv')
    
    print(f'Loading data from {csv_path}')
    df = load_data(csv_path)
    
    summary(df)
    
    # Ejemplo adicional: distribución de ADR
    print("\n=== ADR Distribution ===")
    print(df['adr'].value_counts(bins=5))
    
    # Ejemplo: porcentaje de cancelaciones
    cancel_rate = df['is_canceled'].mean() * 100
    print(f"\nCancellation Rate: {cancel_rate:.2f}%")

if __name__ == "__main__":
    main()
