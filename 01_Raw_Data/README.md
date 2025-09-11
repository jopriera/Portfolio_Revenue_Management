# 01_Raw_Data

This folder contains all raw and synthetic datasets used across the portfolio projects.

## Files

- `kaggle_hotel_booking.csv`  
  • Source: Kaggle Hotel Booking Demand dataset  
  • Contains ~119,000 real bookings with ADR, lead time, country, distribution channel  

- `hotel_booking_clean.csv`  
  • Cleaned version of the Kaggle dataset after initial preprocessing  

- `portfolio.db`  
  • SQLite database containing loaded tables from cleaned CSVs  

- `synthetic_data/synthetic_hotel_bookings.csv`  
  • Generated with SDV to extend historical data and maintain real-world statistical patterns  

## Usage

1. Inspect raw CSVs directly or load into Python/SQL for cleaning.  
2. Synthetic data can be regenerated via `02_Python_Scripts/data_generation.py`.  
3. All datasets should be loaded into `portfolio.db` using `02_Python_Scripts/load_to_sqlite.py` before analysis.
