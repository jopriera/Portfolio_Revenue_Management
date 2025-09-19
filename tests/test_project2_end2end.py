import os
import pandas as pd
import pytest

SCRIPTS_DIR = "Projects/02_Forecasting_Estacional/02_Python_Scripts"
RAW_CSV = "Projects/02_Forecasting_Estacional/01_Raw_Data/forecast_raw.csv"
FORECAST_CSV = "Projects/02_Forecasting_Estacional/01_Raw_Data/forecast_output.csv"
METRICS_JSON = "Projects/02_Forecasting_Estacional/05_Documentation/metrics.json"

def test_forecast_file_created():
    """Checks that forecast_output.csv is created."""
    if not os.path.exists(FORECAST_CSV):
        os.system(f"python {SCRIPTS_DIR}/forecasting.py")
    assert os.path.exists(FORECAST_CSV), "forecast_output.csv does not exist"

def test_evaluate_file_created():
    """Checks that metrics.json is created."""
    if not os.path.exists(METRICS_JSON):
        os.system(f"python {SCRIPTS_DIR}/evaluate_forecast.py")
    assert os.path.exists(METRICS_JSON), "metrics.json does not exist"

def test_metrics_values():
    """Verifies that the metrics have reasonable values."""
    # Load raw data and forecast
    df_raw = pd.read_csv(RAW_CSV)
    df_raw['date'] = pd.to_datetime(
        df_raw['arrival_date_year'].astype(str) + '-' +
        df_raw['arrival_date_month'] + '-' +
        df_raw['arrival_date_day_of_month'].astype(str),
        format='%Y-%B-%d'
    )
    # Filter out zero ADR values and rename columns
    df_actual = df_raw[df_raw['adr'] > 0][['date', 'adr']].rename(columns={'date':'ds','adr':'actual'})
    df_for = pd.read_csv(FORECAST_CSV, parse_dates=['ds']).rename(columns={'yhat':'predicted'})
    metrics = pd.read_json(METRICS_JSON, typ='series')
    # MAPE should be between 0 and 100%
    assert 0 < metrics['mape'] < 100, f"MAPE out of range: {metrics['mape']}"
    # MAE and RMSE must be non-negative
    assert metrics['mae'] >= 0, f"Negative MAE: {metrics['mae']}"
    assert metrics['rmse'] >= 0, f"Negative RMSE: {metrics['rmse']}"