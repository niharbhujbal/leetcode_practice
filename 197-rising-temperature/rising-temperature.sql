# Write your MySQL query statement below
select w.id
from Weather as w
left join Weather as w2 ON datediff(w.recordDate, w2.recordDate)= 1
where w.temperature > w2.temperature