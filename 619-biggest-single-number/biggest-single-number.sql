# Write your MySQL query statement below
SELECT MAX(num) as num
FROM (SELECT num, COUNT(num) as cnt
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1) as s