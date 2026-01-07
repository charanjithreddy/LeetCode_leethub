# Write your MySQL query statement below
select p.project_id,p.employee_id from project p join employee e on p.employee_id=e.employee_id where (project_id,experience_years) in (
select p.project_id,max(e.experience_years) as max_exp from project p left join employee e on p.employee_id=e.employee_id group by p.project_id)