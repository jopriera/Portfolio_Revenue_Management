# 02_Python_Scripts

Python scripts for data generation, cleaning, loading, and exploratory analysis.

## Scripts

- `data_generation.py`  
  • Uses SDV to generate synthetic hotel booking records  
  • Usage: `python data_generation.py`  

- `data_cleaning.py`  
  • Cleans raw CSVs: formats dates, handles missing values, normalizes columns  
  • Usage: `python data_cleaning.py`  

- `load_to_sqlite.py`  
  • Loads cleaned CSVs into `portfolio.db` SQLite database  
  • Usage: `python load_to_sqlite.py`  

- `analysis.py`  
  • Performs EDA: summary statistics, distribution plots, correlation matrix  
  • Usage: `python analysis.py`  

## Requirements

Executed from project root in `rm_portfolio` environment:

pip install pandas numpy sdv sqlalchemy sqlite3


## Notes

- Ensure `01_Raw_Data` contains the latest CSV files.  
- Modify connection string in `load_to_sqlite.py` if using SQL Server Express.
