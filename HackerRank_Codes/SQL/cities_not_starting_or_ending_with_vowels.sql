-- Cities not starting with vowels

-- MySQL solution

SELECT DISTINCT(CITY) FROM STATION WHERE CITY REGEXP '^[^aeiou]';

-- Oracle Solution

SELECT DISTINCT CITY FROM STATION WHERE REGEXP_LIKE(CITY, '^[^AEIOU]');

-- Cities not ending with vowels

-- MySQL Solution

select DISTINCT city from STATION where city NOT REGEXP '[aeiou]$';

-- Oracle Solution

select distinct CITY from STATION where lower(substr(city,length(city),1)) not in ('a','e','i','o','u');

-- Cities not starting or ending with vowels (i.e. no Orange or Miami)

-- MySQL Solution

SELECT DISTINCT(CITY) FROM STATION WHERE CITY NOT REGEXP '^[AEIOUaeiou]' OR City NOT REGEXP '[AEIOUaeiou]$';

-- Oracle Solution

SELECT DISTINCT CITY FROM STATION 
WHERE REGEXP_LIKE(CITY, '^[^AEIOU]') OR lower(substr(city,length(city),1)) not in ('a','e','i','o','u');

-- Cities not starting and not ending with vowels (i.e. no Agra or Anchorage)


-- MySQL Solution

SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[AEIOU]' AND CITY NOT REGEXP '[AEIOU]$';

-- Oracle Solution

SELECT DISTINCT City FROM Station WHERE LOWER(SUBSTR(City,1,1)) NOT IN ('a','e','i','o','u') AND LOWER(SUBSTR(REVERSE(City),1,1)) NOT IN ('a','e','i','o','u');

