# Write your MySQL query statement below
SELECT
d.name AS Department, e.name AS Employee, Salary
FROM Employee e INNER JOIN Department d
ON e.departmentId = d.id
# WHERE departmentId = 1
WHERE Salary = (
    SELECT MAX(Salary) FROM Employee e2
    WHERE e.departmentId = e2.departmentId
)




    