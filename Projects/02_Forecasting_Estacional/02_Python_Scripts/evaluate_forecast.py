"""
evaluate_forecast.py – Forecast Evaluation and Metrics Generation

Purpose:
    Evaluate forecast accuracy and generate metrics for badges and reporting

Usage:
    python evaluate_forecast.py
"""

import os
import json
import pandas as pd
from sklearn.metrics import mean_absolute_error

def calculate_metrics(actual: pd.DataFrame, forecast: pd.DataFrame) -> dict:
    # Merge on 'ds' using original columns 'y' and 'yhat'
    df = pd.merge(actual, forecast, on="ds", how="inner")
    # Rename AFTER merge so we have 'actual' and 'predicted' columns
    df = df.rename(columns={"y": "actual", "yhat": "predicted"})
    return {
        "mae": mean_absolute_error(df["actual"], df["predicted"]),
        "mape": (abs(df["actual"] - df["predicted"]) / df["actual"]).mean() * 100,
    }

def run_evaluation(actual: pd.DataFrame, forecast: pd.DataFrame, out_dir: str) -> dict:
    metrics = calculate_metrics(actual, forecast)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "metrics.json")
    with open(out_file, "w") as f:
        json.dump(metrics, f, indent=2)
    return metrics

def load_data(raw_path: str, forecast_path: str):
    actual = pd.read_csv(raw_path, parse_dates=["ds"])
    forecast = pd.read_csv(forecast_path, parse_dates=["ds"])
    return actual, forecast

def main():
    base = os.path.dirname(__file__)
    raw = os.path.join(base, "../01_Raw_Data/forecast_raw.csv")
    fore = os.path.join(base, "../01_Raw_Data/forecast_output.csv")
    actual, forecast = load_data(raw, fore)
    metrics = run_evaluation(actual, forecast, "../05_Documentation")
    print(metrics)

if __name__ == "__main__":
    main()
