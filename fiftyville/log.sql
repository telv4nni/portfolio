-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Check crime descriptions
SELECT description FROM crime_scene_reports
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND street LIKE 'Humphrey%';

--THEFT TOOK PLACE at 10:15am, witnesses mentions bakery
--Check security cameras at bakery
SELECT activity, license_plate, hour, minute
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10';

--I should check people from license plates
SELECT DISTINCT(name), phone_number, passport_number
FROM people
    JOIN bakery_security_logs
    ON bakery_security_logs.license_plate = people.license_plate
WHERE people.license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE day = '28'
        AND month = '7'
        AND year = '2021'
        AND hour = '10'
        AND minute BETWEEN '10' AND '20');

-- Let's do some interviews
SELECT name, transcript, day, month, year
FROM interviews
WHERE name IN
(SELECT DISTINCT(name)
FROM people
    JOIN bakery_security_logs
    ON bakery_security_logs.license_plate = people.license_plate
WHERE people.license_pl.ate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE day = '28'
        AND month = '7'
        AND year = '2021'
        AND hour = '10'));

-- nothing :(
-- check interviews for "bakery"
SELECT transcript FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE "%bakery%";