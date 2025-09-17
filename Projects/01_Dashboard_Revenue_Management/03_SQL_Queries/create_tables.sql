/*
  Script: create_tables.sql
  Purpose: Schema definition for hotel bookings tables
  Author: Josep Riera
  Date: 2025-09-14
*/

DROP TABLE IF EXISTS hotel_bookings;
CREATE TABLE hotel_bookings (
  hotel_booking_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  hotel                     TEXT NOT NULL,                           -- Hotel type
  is_canceled               INTEGER NOT NULL CHECK(is_canceled IN (0,1)),  -- 0 = not canceled, 1 = canceled
  lead_time                 INTEGER,                                 -- Lead time in days
  arrival_date              TEXT NOT NULL,                           -- Arrival date (YYYY-MM-DD)
  adr                       REAL,                                    -- Average Daily Rate (€)
  agent                     TEXT,                                    -- Agent code
  reservation_status        TEXT,                                    -- Booking status (e.g., Canceled, Checked-In)
  reservation_status_date   TEXT NOT NULL                            -- Status date (YYYY-MM-DD)
);

-- Create an empty synthetic table with identical structure
CREATE TABLE synthetic_bookings AS
SELECT
  hotel_booking_id, hotel, is_canceled, lead_time,
  arrival_date, adr, agent, reservation_status, reservation_status_date
FROM hotel_bookings
WHERE 0;

-- Indexes to improve query performance
CREATE INDEX idx_hotel_bookings_hotel ON hotel_bookings(hotel);
CREATE INDEX idx_hotel_bookings_status_date ON hotel_bookings(reservation_status_date);
