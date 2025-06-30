# Write your MySQL query statement below
select t1.id from Weather t1,Weather t2 where t1.temperature>t2.temperature and DATE_SUB(t1.recordDate,INTERVAL 1 DAY)=t2.recordDate;