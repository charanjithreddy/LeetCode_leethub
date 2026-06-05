# Write your MySQL query statement below
with cte as (select project_id,count(employee_id) as cnt from project group by project_id)
select project_id from cte as t where cnt in (
select max(cnt) as max_cnt from cte as t)