# Write your MySQL query statement below
select e.name as employee
from employee e, employee m
where e.managerID = m.Id
and e.salary > m.salary;

