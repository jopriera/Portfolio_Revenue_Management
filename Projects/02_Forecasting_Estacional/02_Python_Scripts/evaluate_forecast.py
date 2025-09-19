"""
evaluate_forecast.py - Forecast Evaluation and Metrics Generation

Purpose:
    Evaluate forecast accuracy and generate metrics for badges and reporting

Usage:
    python evaluate_forecast.py
"""

import pandas as pd
import json
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import os

def load_data():
    """Load actual and forecast data"""
    actual = pd.read_csv('../01_Raw_Data/forecast_raw.csv')
    # Create a date column combining year, month, and day
    actual['date'] = pd.to_datetime(
        actual['arrival_date_year'].astype(str) + '-' +
        actual['arrival_date_month'] + '-' +
        actual['arrival_date_day_of_month'].astype(str),
        format='%Y-%B-%d'
    )
    actual = actual[['date', 'adr']].rename(columns={'date':'ds', 'adr':'actual'})
    
    forecast = pd.read_csv('../01_Raw_Data/forecast_output.csv', parse_dates=['ds'])
    return actual, forecast

def calculate_metrics(actual, forecast):
    """Calculate forecast accuracy metrics"""
    df = pd.merge(
        actual,
        forecast[['ds','yhat']].rename(columns={'yhat':'predicted'}),
        on='ds',
        how='inner'
    )
    
    if len(df) == 0:
        return {'mae': 0, 'mape': 0, 'samples': 0}
    
    metrics = {
        'mae': mean_absolute_error(df['actual'], df['predicted']),
        'mape': mean_absolute_percentage_error(df['actual'], df['predicted']) * 100,
        'samples': len(df)
    }
    return metrics

def main():
    """Main execution function"""
    actual, forecast = load_data()
    metrics = calculate_metrics(actual, forecast)
    
    # Create folder if it does not exist
    os.makedirs('../05_Documentation', exist_ok=True)
    
    # Save metrics
    with open('../05_Documentation/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    
    print(f"Metrics: MAE={metrics['mae']:.2f}, MAPE={metrics['mape']:.2f}%")

if __name__ == '__main__':
    main()