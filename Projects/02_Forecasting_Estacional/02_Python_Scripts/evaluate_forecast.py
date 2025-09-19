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

def load_data():
    # Load real data
    actual = pd.read_csv('../01_Raw_Data/forecast_raw.csv')
    actual['date'] = pd.to_datetime(
        actual['arrival_date_year'].astype(str) + '-' +
        actual['arrival_date_month'] + '-' +
        actual['arrival_date_day_of_month'].astype(str),
        format='%Y-%B-%d'
    )
    actual = actual[['date', 'adr']].rename(columns={'date':'ds', 'adr':'actual'})
    
    # Filter ADR values = 0 (cancelled reservations or no rate)
    actual = actual[actual['actual'] > 0]
    
    # Load forecast
    forecast = pd.read_csv('../01_Raw_Data/forecast_output.csv', parse_dates=['ds'])
    forecast = forecast[['ds', 'yhat']].rename(columns={'yhat':'predicted'})
    
    return actual, forecast

def calculate_metrics(actual, forecast):
    # Merge only on dates that have ADR > 0
    df = pd.merge(actual, forecast, on='ds', how='inner')
    
    if len(df) == 0:
        return {'error': 'No matching dates between actual and forecast data'}
    
    metrics = {
        'mae': mean_absolute_error(df['actual'], df['predicted']),
        'mape': mean_absolute_percentage_error(df['actual'], df['predicted']) * 100,
        'rmse': ((df['actual'] - df['predicted']) ** 2).mean() ** 0.5,
        'samples': len(df),
        'date_range': f"{df['ds'].min().strftime('%Y-%m-%d')} to {df['ds'].max().strftime('%Y-%m-%d')}"
    }
    return metrics

def main():
    try:
        actual, forecast = load_data()
        metrics = calculate_metrics(actual, forecast)
        
        # Create folder if doesn't exist
        import os
        os.makedirs('../05_Documentation', exist_ok=True)
        
        # Save metrics
        with open('../05_Documentation/metrics.json', 'w') as f:
            json.dump(metrics, f, indent=2)
        
        print(f"Metrics: MAE={metrics['mae']:.2f}, MAPE={metrics['mape']:.2f}%, RMSE={metrics['rmse']:.2f}")
        print(f"Samples: {metrics['samples']}, Date range: {metrics['date_range']}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()