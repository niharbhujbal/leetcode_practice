# Write your MySQL query statement below
WITH first_years AS (
    -- Find the earliest year each product was sold
    SELECT 
        product_id,
        MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id
)
SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
INNER JOIN first_years fy
    ON s.product_id = fy.product_id
    AND s.year = fy.min_year
ORDER BY s.product_id, s.quantity;
