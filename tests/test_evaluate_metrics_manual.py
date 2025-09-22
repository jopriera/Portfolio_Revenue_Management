import pytest
import pandas as pd
import importlib.util
import pathlib


# Locate and load the evaluate_forecast.py module
ROOT = pathlib.Path(__file__).parent.parent.resolve()
MOD_PATH = (
    ROOT
    / "Projects"
    / "02_Forecasting_Estacional"
    / "02_Python_Scripts"
    / "evaluate_forecast.py"
)
spec = importlib.util.spec_from_file_location("eval_mod", str(MOD_PATH))
eval_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval_mod)


def test_calculate_metrics_manual_values():
    """
    Test calculate_metrics with manually defined values:
    actual: [100, 200, 300]
    forecast: [110, 180, 330]
    Expected MAE = 20
    Expected MAPE = 10%
    """
    # Create test DataFrames
    dates = pd.date_range("2021-01-01", periods=3, freq="D")
    actual = pd.DataFrame({"ds": dates, "y": [100, 200, 300]})
    forecast = pd.DataFrame({"ds": dates, "yhat": [110, 180, 330]})

    # Call the function under test
    metrics = eval_mod.calculate_metrics(actual, forecast)

    # Validations
    assert pytest.approx(metrics["mae"], rel=1e-3) == 20.0
    assert pytest.approx(metrics["mape"], rel=1e-3) == 10.0
