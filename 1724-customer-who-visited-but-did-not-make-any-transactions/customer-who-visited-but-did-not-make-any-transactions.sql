# Write your MySQL query statement below
select customer_id, sum(count_no_trans) as count_no_trans
FROM 
(select customer_id, case when transaction_id is NULL THEN 1
ELSE 0 END as count_no_trans -- customer_id, count(transaction_id) as count_no_trans
from Visits as v
LEFT JOIN Transactions as t ON v.visit_id = t.visit_id) as a
GROUP BY customer_id
HAVING sum(count_no_trans) > 0 