/*

Query the median of the Northern Latitudes (LAT_N) from Station and round to 4 decimal places

*/

SELECT ROUND(MEDIAN(LAT_N),4) FROM STATION;