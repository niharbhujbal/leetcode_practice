# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM 
(SELECT e.name as Employee ,d.name as Department,salary as Salary, dense_rank() OVER (PARTITION BY departmentId ORDER BY salary desc) as earn_rank
FROM Employee as e
JOIN Department as d ON e.departmentId = d.id) as a
WHERE earn_rank <= 3