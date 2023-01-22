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

--Thief was withdrawing money and left bakery in about 10 minute time frame. He was talking through the phone for less than a minute. He's taking a flight
--out of Fiftyville tommorow. The person talking thru the phone is buying him ticket.
--The Thief was withdrawing the money at ATM on Leggett Street.
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
SELECT caller, receiver, duration, day, year FROM phone_calls
WHERE year = '2021'
AND month = '7'
AND day = '28'
AND duration < '60'
AND caller IN
(SELECT DISTINCT(phone_number) FROM people
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
OR year = '2021'
AND month = '7'
AND day = '28'
AND duration < '60'
AND receiver IN
(SELECT DISTINCT(phone_number) FROM people
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

--And check who withdrew the money at ATM
SELECT name, amount FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw';

--Maybe compare people from phone calls to ATM users
SELECT caller, receiver, duration, day, year FROM phone_calls
WHERE year = '2021'
AND month = '7'
AND day = '28'
AND duration < '60'
AND caller IN
(SELECT DISTINCT(phone_number) FROM people
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
    AND caller IN
    (SELECT name FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw')
OR year = '2021'
AND month = '7'
AND day = '28'
AND duration < '60'
AND receiver IN
(SELECT DISTINCT(phone_number) FROM people
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
AND receiver IN
(SELECT name FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw');