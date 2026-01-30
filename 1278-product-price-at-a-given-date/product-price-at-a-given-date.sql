WITH MostRecentPriceChanges AS (
    
    SELECT 
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)


SELECT 
    p.product_id,
    COALESCE(mrp.new_price, 10) AS price  
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN MostRecentPriceChanges mrp 
    ON p.product_id = mrp.product_id 
    AND mrp.rn = 1  
ORDER BY p.product_id;