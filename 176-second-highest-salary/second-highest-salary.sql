# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from (select distinct salary from Employee order by salary desc limit 1 offset 1) as m;