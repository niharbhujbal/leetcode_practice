# Write your MySQL query statement below
select a.machine_id,  round(avg(a2.timestamp - a.timestamp),3) as processing_time
from Activity as a
JOIN Activity as a2 on a.machine_id = a2.machine_id and a.process_id = a2.process_id
where a.activity_type = 'start' and a2.activity_type = 'end'
group by a.machine_id