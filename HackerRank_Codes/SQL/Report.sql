/*

Return a report containing three columns:- Name, Mark and Grade
Names of students with grades less than 8 should not be displayed
Order by descending grade, and if students have the same grade, order by marks ascendingly

*/

SELECT 
    CASE 
        WHEN G.Grade > 7 THEN S.Name 
        ELSE 'NULL' 
    END AS Name, 
    G.Grade, 
    S.Marks 
FROM Students S JOIN Grades G 
ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark 
ORDER BY G.Grade DESC, Name ASC, S.Marks ASC;
