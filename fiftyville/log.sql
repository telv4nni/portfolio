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
AND minute BETWEEN 15 AND 25
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
SELECT name, amount FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw';
AND people.name IN
(SELECT DISTINCT(name) FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE people.license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10'
AND minute BETWEEN 15 AND 25
AND activity = 'exit'));

--Check Airports
SELECT * FROM airports;

--Fiftyville is CSF
--Check flights tommorrow
SELECT destination_airport_id, flights.id FROM flights
JOIN airports ON airports.id = flights.origin_airport_id
WHERE year = 2021
AND month = 7
AND day = 29
AND airports.abbreviation = 'CSF'
ORDER BY hour LIMIT 1;

-- Check passengers
SELECT name FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    JOIN flights ON flights.id = passengers.flight_id
    WHERE flights.id IN
    (SELECT flights.id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE year = 2021
    AND month = 7
    AND day = 29
    AND airports.abbreviation = 'CSF' ORDER BY hour LIMIT 1);

-- Compare passengers with ATM
SELECT name FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw'
AND name IN
(
SELECT name FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    JOIN flights ON flights.id = passengers.flight_id
    WHERE flights.id IN
    (SELECT flights.id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE year = 2021
    AND month = 7
    AND day = 29
    AND airports.abbreviation = 'CSF' ORDER BY hour LIMIT 1));

    --Compare last matches with cameras
    SELECT name FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw'
AND name IN
(
SELECT name FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    JOIN flights ON flights.id = passengers.flight_id
    WHERE flights.id IN
    (SELECT flights.id FROM flights
    JOIN airports ON airports.id = flights.origin_airport_id
    WHERE year = 2021
    AND month = 7
    AND day = 29
    AND airports.abbreviation = 'CSF' ORDER BY hour LIMIT 1))
AND name IN(
SELECT name FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
JOIN people ON bank_accounts.person_id = people.id
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE '%Leggett%'
AND transaction_type = 'withdraw'
AND people.name IN
(SELECT DISTINCT(name) FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE people.license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE day = '28'
AND month = '7'
AND year = '2021'
AND hour = '10'
AND minute BETWEEN 15 AND 25
AND activity = 'exit')));

--Ok we have 2 Suspects Now - Bruce and Luca

--Now lets get the phone calls
--Check Luca's and Bruce phone number
SELECT name, phone_number FROM people
WHERE name = 'Luca'
OR name = 'Bruce';

SELECT name FROM people
WHERE phone_number IN
(SELECT caller FROM phone_calls
WHERE year = 2021
AND day = 28
AND month = 7
AND duration < 60)
OR phone_number IN
(SELECT caller FROM phone_calls
WHERE year = 2021
AND day = 28
AND month = 7
AND duration < 60);