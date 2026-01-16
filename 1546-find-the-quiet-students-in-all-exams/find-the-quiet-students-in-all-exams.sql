# Write your MySQL query statement below
select * from student where student_id in (
select distinct(s.student_id) from student s join exam e on s.student_id=e.student_id where s.student_id not in (

select distinct(s.student_id) from student s join exam e on s.student_id=e.student_id where (e.exam_id,e.score) in (
select exam_id,max(score) as scr from exam group by exam_id
union
select exam_id,min(score) as scr from exam group by exam_id
) 
)
)