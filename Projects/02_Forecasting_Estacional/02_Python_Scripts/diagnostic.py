import pandas as pd
import os

def load_actual_data(path):
    """Carga y devuelve el DataFrame de datos reales desde la ruta dada."""
    return pd.read_csv(path)

def load_forecast_data(path):
    """Carga y devuelve el DataFrame de forecast desde la ruta dada."""
    return pd.read_csv(path)

def run_diagnostic(actual_path, forecast_path):
    """
    Ejecuta el diagnóstico: carga ambos CSV, muestra muestras y estadísticas,
    y devuelve una tupla con los DataFrames (actual, forecast).
    """
    actual = load_actual_data(actual_path)
    forecast = load_forecast_data(forecast_path)

    print("Actual data sample:")
    print(actual[['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month', 'adr']].head())
    print(f"\nADR stats: min={actual['adr'].min()}, max={actual['adr'].max()}, mean={actual['adr'].mean()}")

    print("\nForecast data sample:")
    print(forecast[['ds', 'yhat']].head())
    print(f"\nForecast stats: min={forecast['yhat'].min()}, max={forecast['yhat'].max()}, mean={forecast['yhat'].mean()}")

    return actual, forecast

def main():
    base = os.path.dirname(__file__)
    actual_path = os.path.join(base, '../01_Raw_Data/forecast_raw.csv')
    forecast_path = os.path.join(base, '../01_Raw_Data/forecast_output.csv')
    run_diagnostic(actual_path, forecast_path)

if __name__ == '__main__':
    main()
