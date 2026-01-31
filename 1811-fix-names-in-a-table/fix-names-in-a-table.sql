# Write your MySQL query statement below
SELECT 
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),     -- First character uppercase
        LOWER(SUBSTRING(name, 2))         -- Remaining characters lowercase
    ) AS name
FROM Users
ORDER BY user_id;