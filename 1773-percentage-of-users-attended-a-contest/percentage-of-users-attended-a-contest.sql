# Write your MySQL query statement below
SELECT m.contest_id, round(count(r2.user_id) * 100/ count(m.user_id),2) as percentage
FROM (SELECT *
FROM Users as u
CROSS JOIN (SELECT DISTINCT contest_id FROM Register) as r) as m
LEFT JOIN Register as r2 ON r2.user_id = m.user_id and m.contest_id = r2.contest_id
GROUP BY m.contest_id
ORDER BY percentage desc, m.contest_id