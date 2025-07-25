# Write your MySQL query statement below
select Department,Employee,Salary from (select d.name as Department,e.name as Employee,e.salary as Salary, dense_rank() over(partition by d.id order by e.salary desc) as rnk from Department d left join Employee e on d.id=e.departmentId) as t where rnk<=3 and Employee is not null
;