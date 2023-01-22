-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Check crime descriptions
SELECT description FROM crime_scene_reports
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND street LIKE 'Humphrey%';
--THEFT TOOK PLACE at 10:15am, witnesses mentions bakery
--Check security cameras at bakery
SELECT activity, license_plate
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10';
