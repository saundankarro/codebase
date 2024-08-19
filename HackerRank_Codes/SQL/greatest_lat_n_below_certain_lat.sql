/*
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. 
Truncate your answer to  decimal places.
*/

-- MySQL
select ROUND(max(LAT_N),4) FROM STATION WHERE LAT_N < 137.2345;

-- Oracle
select ROUND(max(LAT_N),4) FROM STATION WHERE LAT_N < 137.2345;