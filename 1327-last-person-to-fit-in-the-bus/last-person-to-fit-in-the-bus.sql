# Write your MySQL query statement below
with cte as (SELECT *, SUM(Weight) OVER (ORDER BY turn) as cum_sum
FROM Queue)

SELECT person_name
FROM cte
WHERE cum_sum <= 1000
ORDER BY turn desc
limit 1