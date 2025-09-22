import shutil
import pathlib
import pandas as pd
import pytest
import importlib.util
import os

ROOT = pathlib.Path(__file__).parent.parent.resolve()
DIAG_PATH = ROOT / "Projects" / "02_Forecasting_Estacional" / "02_Python_Scripts" / "diagnostic.py"

spec = importlib.util.spec_from_file_location("diag_mod", str(DIAG_PATH))
diag_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diag_mod)


def test_run_diagnostic(tmp_path):
    src_actual = ROOT / "Projects" / "02_Forecasting_Estacional" / "01_Raw_Data" / "forecast_raw.csv"
    src_forecast = ROOT / "Projects" / "02_Forecasting_Estacional" / "01_Raw_Data" / "forecast_output.csv"
    dst_actual = tmp_path / "forecast_raw.csv"
    dst_forecast = tmp_path / "forecast_output.csv"
    shutil.copy(src_actual, dst_actual)
    shutil.copy(src_forecast, dst_forecast)

    actual, forecast = diag_mod.run_diagnostic(str(dst_actual), str(dst_forecast))

    assert isinstance(actual, pd.DataFrame)
    assert isinstance(forecast, pd.DataFrame)
    assert "yhat" in forecast.columns