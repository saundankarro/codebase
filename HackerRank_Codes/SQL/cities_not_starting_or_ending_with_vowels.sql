-- MySQL solution

SELECT DISTINCT(CITY) FROM STATION WHERE CITY REGEXP '^[^aeiou]';

-- Oracle Solution

SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY, '^[^AEIOU]');

-- MySQL Solution

select DISTINCT city from STATION where city NOT REGEXP '[aeiou]$';

-- Oracle Solution

select distinct CITY from STATION where lower(substr(city,length(city),1)) not in ('a','e','i','o','u');