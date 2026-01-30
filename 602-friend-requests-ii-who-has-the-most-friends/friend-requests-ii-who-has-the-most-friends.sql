# Write your MySQL query statement below

SELECT id, SUM(nums) as num
FROM (SELECT requester_id as id, COUNT(accepter_id) as nums
FROM RequestAccepted
GROUP BY requester_id
UNION ALL
SELECT accepter_id as id, COUNT(requester_id) as nums
FROM RequestAccepted
GROUP BY accepter_id) as a
GROUP BY id
ORDER BY num desc
LIMIT 1