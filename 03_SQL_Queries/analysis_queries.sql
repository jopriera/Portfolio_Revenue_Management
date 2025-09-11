-- analysis_queries.sql
-- Example queries to explore and validate hotel booking data

-- 1. Count records by hotel and cancellation status
SELECT
    hotel,
    is_canceled,
    COUNT(*) AS total
FROM hotel_bookings
GROUP BY hotel, is_canceled;

-- 2. Average ADR by hotel type
SELECT
    hotel,
    ROUND(AVG(adr), 2) AS avg_adr
FROM hotel_bookings
GROUP BY hotel;

-- 3. Overall cancellation rate as a percentage
SELECT
    ROUND(100.0 * SUM(is_canceled) / COUNT(*), 2) AS cancellation_rate_pct
FROM hotel_bookings;

-- 4. Monthly booking volume by reservation date
SELECT
    STRFTIME('%Y-%m', reservation_status_date) AS month,
    COUNT(*) AS bookings
FROM hotel_bookings
GROUP BY month
ORDER BY month;
