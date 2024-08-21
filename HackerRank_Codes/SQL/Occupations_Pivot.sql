/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its 
corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

The first column is an alphabetically ordered list of Doctor names.
The second column is an alphabetically ordered list of Professor names.
The third column is an alphabetically ordered list of Singer names.
The fourth column is an alphabetically ordered list of Actor names.
The empty cell data for columns with less than the maximum number of names per occupation 
    (in this case, the Professor and Actor columns) are filled with NULL values.
*/

SELECT 
    NVL(MAX(CASE WHEN occupation = 'Doctor' THEN name END), 'NULL') AS Doctor, 
    NVL(MAX(CASE WHEN occupation = 'Professor' THEN name END), 'NULL') AS Professor, 
    NVL(MAX(CASE WHEN occupation = 'Singer' THEN name END), 'NULL') AS Singer, 
    NVL(MAX(CASE WHEN occupation = 'Actor' THEN name END), 'NULL') AS Actor 
FROM (
    SELECT 
        name, 
        occupation, 
        ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) AS rn 
    FROM OCCUPATIONS
    ) 
GROUP BY rn 
ORDER BY rn;

/*

OUTPUT:

Aamina Ashley Christeen Eve 
Julia Belvet Jane Jennifer 
Priya Britney Jenny Ketty 
NULL Maria Kristeen Samantha 
NULL Meera NULL NULL 
NULL Naomi NULL NULL 
NULL Priyanka NULL NULL


*/