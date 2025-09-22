import pathlib
import json
import pandas as pd
import pytest
import importlib.util

ROOT = pathlib.Path(__file__).parent.parent.resolve()
MOD_PATH = ROOT / "Projects" / "02_Forecasting_Estacional" / "02_Python_Scripts" / "evaluate_forecast.py"

spec = importlib.util.spec_from_file_location("eval_mod", str(MOD_PATH))
eval_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval_mod)

def test_run_evaluation_creates_metrics_json(tmp_path):
    dates = pd.date_range("2021-01-01", periods=5, freq="D")
    actual = pd.DataFrame({"ds": dates, "y": [10,20,30,40,50]})
    forecast = pd.DataFrame({"ds": dates, "yhat": [12,18,33,39,52]})

    out_dir = str(tmp_path / "05_Documentation")
    metrics = eval_mod.run_evaluation(actual, forecast, out_dir)

    assert set(metrics.keys()) == {"mae", "mape"}

    file = pathlib.Path(out_dir) / "metrics.json"
    assert file.exists()
    data = json.loads(file.read_text())
    assert data == metrics

def test_calculate_metrics_with_known_values():
    """Test calculate_metrics with manually verifiable data."""
    dates = pd.date_range("2021-01-01", periods=3, freq="D")
    # actual: [100, 200, 300], predicted: [110, 180, 330]
    actual = pd.DataFrame({"ds": dates, "y": [100, 200, 300]})
    forecast = pd.DataFrame({"ds": dates, "yhat": [110, 180, 330]})

    metrics = eval_mod.calculate_metrics(actual, forecast)

    # Manual calculations:
    # MAE = (|100-110| + |200-180| + |300-330|) / 3 = 20
    # MAPE = ((10/100 + 20/200 + 30/300) / 3) * 100 = 10%
    assert abs(metrics["mae"] - 20.0) < 0.01, f"Expected MAE=20, got {metrics['mae']}"
    assert abs(metrics["mape"] - 10.0) < 0.01, f"Expected MAPE=10, got {metrics['mape']}"
