# Write your MySQL query statement below
with cte as (SELECT *, LAG(student, 1) OVER (ORDER BY id) as even, LEAD(student, 1) OVER (ORDER BY id) as odd
FROM Seat)

SELECT id, COALESCE(CASE WHEN id%2 = 0 THEN even WHEN id%2 = 1 THEN odd END, cte.student) as student
FROM cte