# Write your MySQL query statement below
select project_id from (
select project_id,count(employee_id) as cnt from project group by project_id) as t where cnt in (
select max(cnt) as max_cnt from (select count(employee_id) as cnt from project p group by project_id) as t)