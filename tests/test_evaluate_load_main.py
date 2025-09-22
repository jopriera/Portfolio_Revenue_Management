import os
import pytest
import pandas as pd
import importlib.util
import pathlib

# Path and load of the evaluate_forecast.py module
ROOT = pathlib.Path(__file__).parent.parent.resolve()
MOD_PATH = ROOT / "Projects" / "02_Forecasting_Estacional" / "02_Python_Scripts" / "evaluate_forecast.py"
spec = importlib.util.spec_from_file_location("eval_mod", str(MOD_PATH))
eval_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval_mod)

def test_load_data(tmp_path):
    # Create temporary CSVs with minimal data for load_data
    actual_csv = tmp_path / "actual.csv"
    forecast_csv = tmp_path / "forecast.csv"

    actual_data = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=3),
        "y": [100, 110, 105]
    })
    forecast_data = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=3),
        "yhat": [102, 108, 107]
    })

    actual_data.to_csv(actual_csv, index=False)
    forecast_data.to_csv(forecast_csv, index=False)

    # Load with the function to be tested
    actual_loaded, forecast_loaded = eval_mod.load_data(str(actual_csv), str(forecast_csv))

    # Verify DataFrames load correctly and with expected columns
    assert list(actual_loaded.columns) == ["ds", "y"]
    assert list(forecast_loaded.columns) == ["ds", "yhat"]
    assert len(actual_loaded) == 3
    assert len(forecast_loaded) == 3

def test_main_prints_metrics(tmp_path, capsys):
    # Create CSVs with minimal data to run main()
    base_path = tmp_path
    raw_path = base_path / "forecast_raw.csv"
    fore_path = base_path / "forecast_output.csv"

    actual_data = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=3),
        "y": [100, 110, 105]
    })
    forecast_data = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=3),
        "yhat": [102, 108, 107]
    })

    actual_data.to_csv(raw_path, index=False)
    forecast_data.to_csv(fore_path, index=False)

    # Monkey-patch os.path.join so that any joined path resolves to our tmp files
    original_join = eval_mod.os.path.join
    eval_mod.os.path.join = lambda *args: str(base_path / pathlib.Path(args[-1]).name)

    try:
        # Run main (it will use our tmp_path CSVs)
        eval_mod.main()
    finally:
        # Restore the original join
        eval_mod.os.path.join = original_join

    # Capture printed output and verify metrics keys
    captured = capsys.readouterr()
    assert "mae" in captured.out.lower()
    assert "mape" in captured.out.lower()
