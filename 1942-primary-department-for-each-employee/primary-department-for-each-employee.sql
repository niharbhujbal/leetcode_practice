# Write your MySQL query statement below
# if emplyee is in his primary deparment then it will have N flag else employee has one primary depatment
SELECT 
    employee_id,
    department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT 
    employee_id,
    department_id
FROM Employee
WHERE employee_id IN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) = 1
);