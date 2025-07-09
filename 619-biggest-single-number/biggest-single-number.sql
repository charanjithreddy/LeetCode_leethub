# Write your MySQL query statement below
select max(num) as num from (select num,count(num) as cnt from MyNumbers group by num having count(num)=1) as t;