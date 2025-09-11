# 03_SQL_Queries

Contains SQL scripts for database schema creation and analytical queries.

## Files

- `create_tables.sql`  
  • Defines tables for bookings, segments, channels, and synthetic data  
  • Usage: run against `portfolio.db` or SQL Server  

- `analysis_queries.sql`  
  • Collection of revenue and occupancy analysis queries  
  • Examples:
    - Monthly ADR by hotel type  
    - Cancellation rate per segment  
    - Forecasting preparation queries  

## How to Run

1. Open your SQL client (SQLite CLI or SQL Server Management Studio).  
2. Execute `create_tables.sql` to set up schema.  
3. Run `analysis_queries.sql` to generate result sets for dashboards.
