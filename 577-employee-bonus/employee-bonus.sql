# Write your MySQL query statement below
select name, bonus
FROM Employee as e
LEFT JOIN Bonus as b ON b.empId = e.empId
WHERE bonus is NULL OR bonus < 1000