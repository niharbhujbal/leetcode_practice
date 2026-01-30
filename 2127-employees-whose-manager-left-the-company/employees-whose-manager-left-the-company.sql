# Write your MySQL query statement below
SELECT e1.employee_id
FROM Employees as e1
LEFT JOIN Employees as e2 ON e2.employee_id = e1.manager_id
WHERE e2.name is NULL and e1.manager_id is not NULL and e1.salary < 30000
ORDER BY e1.employee_id