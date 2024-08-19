/*
    Select name of students who scored more than 75 and order by last three letters of name and id ascending
*/

-- Oracle Solution
SELECT name FROM students WHERE marks > 75 ORDER BY substr(name,LENGTH(name)-2,3), id;

-- MySQL Solution
select name
from students
where marks > 75 
order by right(name,3) asc, id asc;