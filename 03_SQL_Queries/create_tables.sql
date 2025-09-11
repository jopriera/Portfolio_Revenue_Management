-- create_tables.sql
-- Define the schema for hotel bookings tables

DROP TABLE IF EXISTS hotel_bookings;
CREATE TABLE hotel_bookings (
    hotel_booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel TEXT,
    is_canceled INTEGER,
    lead_time INTEGER,
    arrival_date DATE,
    adr REAL,
    agent TEXT,
    reservation_status TEXT,
    reservation_status_date DATE
    -- Add additional columns as needed to match your CSV
);

DROP TABLE IF EXISTS synthetic_bookings;
CREATE TABLE synthetic_bookings AS
SELECT * FROM hotel_bookings WHERE 0;  -- Create empty table with same structure
