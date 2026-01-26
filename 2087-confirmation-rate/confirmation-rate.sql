# Write your MySQL query statement below
SELECT s.user_id, round(ifnull(confirmation_rate, 0.00),2) as confirmation_rate
FROM Signups as s
LEFT JOIN (
SELECT *, AVG(CASE WHEN action = 'confirmed' THEN 1 else 0 END) as confirmation_rate
FROM Confirmations
GROUP BY user_id) as c ON s.user_id = c.user_id
