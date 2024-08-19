-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION.

SELECT DISTINCT(CITY) FROM STATION
WHERE CITY like 'A%' or city like 'E%' or city like 'I%' or city like 'O%' or city like 'U%';

-- Query the list of CITY names ending with vowels (i.e., a, e, i, o, or u) from STATION.

SELECT DISTINCT(CITY) FROM STATION
WHERE CITY like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';

-- Query list of CITY names starting and ending with vowels from STATION

SELECT DISTINCT(CITY) FROM STATION
WHERE CITY like 'A%a' or city like 'A%e' or city like 'A%i' or city like 'A%o' or city like 'A%u'
OR CITY like 'E%a' or city like 'E%e' or city like 'E%i' or city like 'E%o' or city like 'E%u'
OR CITY like 'I%a' or city like 'I%e' or city like 'I%i' or city like 'I%o' or city like 'I%u'
OR CITY like 'O%a' or city like 'O%e' or city like 'O%i' or city like 'O%o' or city like 'O%u'
OR CITY like 'U%a' or city like 'U%e' or city like 'U%i' or city like 'U%o' or city like 'U%u'
;
