# Portfolio_Revenue_Management

Este repositorio contiene proyectos de Revenue Management y Business Intelligence aplicados a la industria hotelera.

## Estructura de Carpetas

```
Portfolio_Revenue_Management/
├── 01_Raw_Data/
│   ├── kaggle_hotel_booking.csv
│   ├── synthetic_data/
│   │   └── synthetic_hotel_bookings.csv
├── 02_Python_Scripts/
│   ├── data_generation.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── load_to_sqlite.py
├── 03_SQL_Queries/
│   ├── create_tables.sql
│   └── analysis_queries.sql
├── 04_PowerBI_Files/
│   └── Portfolio_Hotel_Revenue_Management_Dashboard_JosepRiera.pbix
├── 05_Documentation/
│   └── dashboard_screenshot.png
└── portfolio.db
```

## Proyecto #1: Hotel Revenue Management Dashboard

- **Archivo Power BI**: `04_PowerBI_Files/Portfolio_Hotel_Revenue_Management_Dashboard_JosepRiera.pbix`  
- **Captura de pantalla**:

  ![Dashboard Final](05_Documentation/dashboard_screenshot.png)

- **Descripción**:  
  Dashboard interactivo que permite:
  - Visualizar **Average ADR (€)**, **Average Length of Stay** y **Cancellation Rate (%)**  
  - Comparar **Average ADR by Hotel Type** con línea de promedio de portfolio  
  - Ver tendencia mensual de volumen de reservas  
  - Filtrar dinámicamente por **Market Segment** y **Country**

## Prerrequisitos

- **Software**  
  - Power BI Desktop (Windows)  
  - Anaconda con Python 3.10+  
  - SQLite (macOS) / SQL Server Express (Windows)  
  - Git y GitHub CLI (recomendado)

- **Librerías Python**  
  Crear entorno y luego:
  ```bash
  pip install pandas numpy sdv faker matplotlib seaborn plotly scikit-learn sqlalchemy jupyter
  ```

## Pasos para reproducir

1. Clonar el repositorio  
   ```bash
   git clone git@github.com:jopriera/Portfolio_Revenue_Management.git
   cd Portfolio_Revenue_Management
   ```
2. Configurar entorno Python  
   ```bash
   conda create -n rm_portfolio python=3.10 -y
   conda activate rm_portfolio
   pip install pandas numpy sdv faker matplotlib seaborn plotly scikit-learn sqlalchemy jupyter
   ```
3. Descargar datos y colocarlos en `01_Raw_Data/`  
4. (Opcional) Generar datos sintéticos  
   ```bash
   python 02_Python_Scripts/data_generation.py
   ```
5. Cargar datos en SQLite  
   ```bash
   cd 02_Python_Scripts
   python load_to_sqlite.py
   ```
6. Abrir dashboard en Power BI Desktop  
   - Navegar a `04_PowerBI_Files/Portfolio_Hotel_Revenue_Management_Dashboard_JosepRiera.pbix` y abrir.

## Skills Demostrados

- Python: pandas, SDV, SQLite  
- SQL: SQLite  
- Power BI: DAX, visualizaciones interactivas  
- Data Visualization & EDA

## Próximos Pasos

Proyecto #2: Análisis de Cancelaciones y Segmentación Avanzada

---

Para feedback o dudas, abre un issue o contáctame por LinkedIn.