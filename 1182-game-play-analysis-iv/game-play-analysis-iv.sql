# Write your MySQL query statement below

SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id)
FROM Activity),2) as fraction
FROM Activity as a
JOIN Activity as a2 ON datediff(a2.event_date, a.event_date) = 1 and a.player_id = a2.player_id
WHERE (a.player_id, a.event_date) IN (
    -- Identify each player's first login date
    SELECT 
        player_id,
        MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)
