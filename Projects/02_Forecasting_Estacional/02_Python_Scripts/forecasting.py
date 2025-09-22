"""
forecasting.py - Revenue Management Forecasting with Prophet

Purpose:
    Generate occupancy forecasts for the next 3 months using Facebook Prophet.

Dependencies:
    pandas, prophet, scikit-learn (see requirements.txt)

Usage:
    python forecasting.py

Author: Josep Riera Querol
Date: September 2025
"""

import pandas as pd
import logging
from prophet import Prophet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
input_path = '../01_Raw_Data/forecast_raw.csv'
output_path = '../01_Raw_Data/forecast_output.csv'

def load_and_validate_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(
        df['arrival_date_year'].astype(str) + '-' +
        df['arrival_date_month'] + '-' +
        df['arrival_date_day_of_month'].astype(str),
        format='%Y-%B-%d'
    )
    df = df[['date', 'adr']].rename(columns={'date':'ds', 'adr':'y'})
    return df

def create_prophet_model():
    m = Prophet(daily_seasonality=False, weekly_seasonality=True, yearly_seasonality=True)
    return m

def generate_forecast(model, df, periods=90):
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def save_results(forecast, output_path):
    forecast[['ds','yhat']].to_csv(output_path, index=False)

def run_forecast():
    """
    run_forecast: load data, train Prophet model, generate forecast, and save results.
    Separated for testing and coverage measurement.
    """
    df = load_and_validate_data(input_path)
    model = create_prophet_model()
    forecast = generate_forecast(model, df)
    save_results(forecast, output_path)
    logger.info('Forecast completed and saved.')

def main():
    run_forecast()

if __name__ == '__main__':
    main()
