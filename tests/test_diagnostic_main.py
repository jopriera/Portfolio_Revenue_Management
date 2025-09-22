import os
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


def test_main_executes_run_diagnostic(tmp_path, capsys, monkeypatch):
    # Prepare minimal CSVs named as in main()
    raw_dir = tmp_path / "01_Raw_Data"
    raw_dir.mkdir(parents=True)
    actual_csv = raw_dir / "forecast_raw.csv"
    forecast_csv = raw_dir / "forecast_output.csv"

    # Create dummy data
    pd.DataFrame({
        "arrival_date_year": [2025],
        "arrival_date_month": ["March"],
        "arrival_date_day_of_month": [15],
        "adr": [123.0]
    }).to_csv(actual_csv, index=False)

    pd.DataFrame({
        "ds": ["2025-03-15"],
        "yhat": [130.0]
    }).to_csv(forecast_csv, index=False)

    # Create scripts dir so that relative path works
    scripts_dir = tmp_path / "02_Python_Scripts"
    scripts_dir.mkdir()

    # Monkey-patch dirname so main() uses tmp_path/02_Python_Scripts as base
    monkeypatch.setattr(diag_mod.os.path, "dirname", lambda _: str(scripts_dir))

    # Execute main()
    diag_mod.main()

    # Capture output
    captured = capsys.readouterr()
    out = captured.out
    assert "Actual data sample:" in out
    assert "Forecast data sample:" in out