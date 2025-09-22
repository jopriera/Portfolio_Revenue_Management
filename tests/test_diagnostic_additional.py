import pytest
import pandas as pd
import importlib.util
import pathlib

# Path and load of the diagnostic.py module
ROOT = pathlib.Path(__file__).parent.parent.resolve()
MOD_PATH = ROOT / "Projects" / "02_Forecasting_Estacional" / "02_Python_Scripts" / "diagnostic.py"
spec = importlib.util.spec_from_file_location("diag_mod", str(MOD_PATH))
diag_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diag_mod)

def test_load_actual_and_forecast_data(tmp_path):
    # Create minimal CSVs for actual and forecast
    actual_csv = tmp_path / "actual.csv"
    forecast_csv = tmp_path / "forecast.csv"

    actual_df = pd.DataFrame({
        "arrival_date_year": [2023, 2023],
        "arrival_date_month": ["January", "January"],
        "arrival_date_day_of_month": [1, 2],
        "adr": [100.0, 150.0]
    })
    forecast_df = pd.DataFrame({
        "ds": ["2023-01-01", "2023-01-02"],
        "yhat": [110.0, 140.0]
    })

    actual_df.to_csv(actual_csv, index=False)
    forecast_df.to_csv(forecast_csv, index=False)

    # Test load_actual_data
    loaded_actual = diag_mod.load_actual_data(str(actual_csv))
    assert isinstance(loaded_actual, pd.DataFrame)
    assert list(loaded_actual.columns) == ["arrival_date_year", "arrival_date_month", "arrival_date_day_of_month", "adr"]
    assert len(loaded_actual) == 2

    # Test load_forecast_data
    loaded_forecast = diag_mod.load_forecast_data(str(forecast_csv))
    assert isinstance(loaded_forecast, pd.DataFrame)
    assert list(loaded_forecast.columns) == ["ds", "yhat"]
    assert len(loaded_forecast) == 2

def test_run_diagnostic_prints_and_returns(tmp_path, capsys):
    # Create minimal CSVs for diagnostic
    actual_csv = tmp_path / "forecast_raw.csv"
    forecast_csv = tmp_path / "forecast_output.csv"

    actual_df = pd.DataFrame({
        "arrival_date_year": [2023],
        "arrival_date_month": ["February"],
        "arrival_date_day_of_month": [10],
        "adr": [200.0]
    })
    forecast_df = pd.DataFrame({
        "ds": ["2023-02-10"],
        "yhat": [210.0]
    })

    actual_df.to_csv(actual_csv, index=False)
    forecast_df.to_csv(forecast_csv, index=False)

    # Monkey-patch dirname so that run_diagnostic reads from tmp_path
    original_dirname = diag_mod.os.path.dirname
    diag_mod.os.path.dirname = lambda _: str(tmp_path)

    try:
        actual_ret, forecast_ret = diag_mod.run_diagnostic(str(actual_csv), str(forecast_csv))
    finally:
        diag_mod.os.path.dirname = original_dirname

    # Verify return types
    assert isinstance(actual_ret, pd.DataFrame)
    assert isinstance(forecast_ret, pd.DataFrame)

    # Capture and assert printed output
    captured = capsys.readouterr()
    out = captured.out
    assert "Actual data sample:" in out
    assert "ADR stats:" in out
    assert "Forecast data sample:" in out
    assert "Forecast stats:" in out