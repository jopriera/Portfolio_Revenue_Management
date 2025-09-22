import os
import shutil
import tempfile
import pandas as pd
import pytest
import importlib.util

# 1. Localiza el fichero forecasting.py en tu proyecto
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
MODULE_PATH = os.path.join(
    ROOT,
    "Projects",
    "02_Forecasting_Estacional",
    "02_Python_Scripts",
    "forecasting.py",
)

# 2. Carga el módulo desde su ruta de fichero
spec = importlib.util.spec_from_file_location("forecasting_mod", MODULE_PATH)
forecasting_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(forecasting_mod)

@pytest.fixture(autouse=True)
def setup_paths(tmp_path):
    """
    Copia forecast_raw.csv a tmp y parchea las variables input_path/output_path
    directamente en el módulo cargado.
    """
    src = os.path.join(
        ROOT,
        "Projects",
        "02_Forecasting_Estacional",
        "01_Raw_Data",
        "forecast_raw.csv",
    )
    dst_raw = tmp_path / "forecast_raw.csv"
    dst_out = tmp_path / "forecast_output.csv"

    shutil.copy(src, dst_raw)

    # Parchea los paths dentro del módulo
    forecasting_mod.input_path = str(dst_raw)
    forecasting_mod.output_path = str(dst_out)

    return dst_out

def test_run_forecast_creates_file(setup_paths):
    """
    Ejecuta run_forecast() del módulo cargado y verifica el CSV de salida.
    """
    forecasting_mod.run_forecast()
    out = setup_paths
    assert out.exists(), "No se creó forecast_output.csv"

    df = pd.read_csv(out, parse_dates=["ds"])
    assert "yhat" in df.columns, "Falta la columna 'yhat'"
    assert len(df) > 90, "El número de filas es menor o igual a 90"
