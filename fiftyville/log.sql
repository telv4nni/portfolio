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

--Thief was withdrawing money and left bakery in about 10 minute time frame. He was talking through the phone for less than a minute
--Let's check cameras again
SELECT license_plate, hour, minute
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10'
AND minute BETWEEN 5 AND 25
AND activity = 'exit';

--Great now let's check the phone calls
SELECT caller, receiver FROM phone_calls
WHERE caller IN
(SELECT DISTINCT(people.name) FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE people.license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10'
AND minute BETWEEN 5 AND 25
AND activity = 'exit'))
OR receiver IN
(SELECT DISTINCT(people.name) FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE people.license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10'
AND minute BETWEEN 5 AND 25
AND activity = 'exit'));