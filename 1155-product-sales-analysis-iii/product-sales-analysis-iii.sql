# Write your MySQL query statement below
SELECT product_id, year as first_year, quantity, price
FROM (SELECT *, rank() OVER (PARTITION BY product_id ORDER BY year) as prod_yrs
FROM Sales) as cte
WHERE prod_yrs = 1
