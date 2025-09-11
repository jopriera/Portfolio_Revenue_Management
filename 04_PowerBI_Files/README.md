# 04_PowerBI_Files

Power BI reports and dashboards for revenue management analysis.

## File

- `Revenue_Dashboard.pbix`  
  • Interactive dashboard with:
    - Cards for Average ADR, Length of Stay, Cancellation Rate  
    - Bar chart: ADR by Hotel Type vs. portfolio average  
    - Line chart: Monthly booking volume trend  
    - Filters: Market Segment, Country  

## How to Open

1. Install Power BI Desktop (Windows).  
2. Open `Revenue_Dashboard.pbix`.  
3. Verify data source connections point to `portfolio.db` or CSV files in `01_Raw_Data`.  

## Key DAX Measures

- `AvgADR = AVERAGE(Bookings[ADR])`  
- `CancellationRate = DIVIDE(COUNTROWS(FILTER(Bookings, Bookings[Status]="Canceled")), COUNTROWS(Bookings))`  

## Insights

- Resort hotels show a 7% higher ADR than city hotels.  
- Peak booking volume occurs in July and August each year.  
- Cancellation rate spikes during off-peak months.
