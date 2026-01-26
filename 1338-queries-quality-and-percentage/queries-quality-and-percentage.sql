# Write your MySQL query statement below
SELECT query_name, round(AVG(rating / position),2) as quality, round(AVG(CASE WHEN rating < 3 THEN 100 ELSE 0 END),2) as poor_query_percentage
FROM Queries
GROUP BY query_name