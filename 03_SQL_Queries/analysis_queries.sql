/*
  Script: analysis_queries.sql
  Purpose: Key KPIs for hotel booking data exploration and validation
  Author: Josep Riera
  Date: 2025-09-14
*/

-- 1. Total bookings by hotel type and cancellation status
SELECT
  hotel AS HotelType,
  is_canceled AS CanceledFlag,
  COUNT(*) AS TotalBookings
FROM hotel_bookings
GROUP BY hotel, is_canceled;

-- 2. Average ADR by hotel type
SELECT
  hotel AS HotelType,
  ROUND(AVG(adr), 2) AS AvgADR
FROM hotel_bookings
GROUP BY hotel;

-- 3. Overall cancellation rate (%)
SELECT
  ROUND(100.0 * SUM(is_canceled) / COUNT(*), 2) AS CancellationRatePct
FROM hotel_bookings;

-- 4. Monthly booking volume by reservation status date
SELECT
  STRFTIME('%Y-%m', reservation_status_date) AS Month,
  COUNT(*) AS BookingCount
FROM hotel_bookings
GROUP BY Month
ORDER BY Month;
