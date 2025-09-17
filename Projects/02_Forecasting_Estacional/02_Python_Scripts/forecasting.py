\"\"\"
forecasting.py - Revenue Management Forecasting with Prophet

Purpose:
    Generate occupancy forecasts for the next 3 months using Facebook Prophet.

Dependencies:
    pandas, prophet, scikit-learn (see requirements.txt)

Usage:
    python forecasting.py

Author: Josep Riera Querol
Date: September 2025
\"\"\"

import pandas as pd
import numpy as np
import logging
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_and_validate_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'])
    df = df.rename(columns={'date':'ds','occupancy':'y'})
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

def main():
    input_path = '../01_Raw_Data/forecast_raw.csv'
    output_path = '../01_Raw_Data/forecast_output.csv'
    df = load_and_validate_data(input_path)
    model = create_prophet_model()
    forecast = generate_forecast(model, df)
    save_results(forecast, output_path)
    logger.info('Forecast completed and saved.')

if __name__ == '__main__':
    main()
