# Write your MySQL query statement below
WITH DailyTotals AS (
    -- Step 1: Aggregate amounts per day (handle multiple customers per date)
    SELECT 
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
MovingWindow AS (
    -- Step 2: Compute 7-day moving sum using window function
    SELECT 
        visited_on,
        daily_amount,
        -- Moving sum: current row + 6 preceding rows = 7 days total
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS moving_sum,
        -- Count rows in window to ensure we have full 7 days
        ROW_NUMBER() OVER (ORDER BY visited_on) AS row_num
    FROM DailyTotals
)
-- Step 3: Filter to dates with complete 7-day window and compute average
SELECT 
    visited_on,
    moving_sum AS amount,
    ROUND(moving_sum / 7, 2) AS average_amount
FROM MovingWindow
WHERE row_num >= 7  -- Only include dates with at least 6 preceding days
ORDER BY visited_on;