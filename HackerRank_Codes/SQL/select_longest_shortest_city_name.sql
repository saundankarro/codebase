/*
    Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths 
    (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that 
    comes first when ordered alphabetically.
*/

-- Two Query ANSWER
SELECT CITY, LENGTH(CITY) FROM STATION WHERE LENGTH(CITY) = ( SELECT MIN(LENGTH(CITY)) FROM STATION ) ORDER BY CITY LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION WHERE LENGTH(CITY) = ( SELECT MAX(LENGTH(CITY)) FROM STATION ) LIMIT 1;

-- One Query Answer
select city, LENGTH(city) length from Station
where id in (
    (select id from station order by Length(city), city limit 1),
    (select id from station order by Length(city) desc, city limit 1)
);
