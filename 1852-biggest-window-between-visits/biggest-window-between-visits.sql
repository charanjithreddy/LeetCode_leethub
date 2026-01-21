# Write your MySQL query statement below
with temp as (
    select *,row_number() over (partition by user_id order by visit_date) as rnk from 
    (select * from uservisits
    union all
    select distinct(user_id) as user_id,str_to_date('2021-1-1','%Y-%m-%d') as visit_date from uservisits
    ) as t
)
select user_id,max(diff) as biggest_window from (
select t1.user_id,datediff(t2.visit_date,t1.visit_date) as diff from temp t1 join temp t2 on t1.user_id=t2.user_id and t1.rnk+1=t2.rnk) as t1 group by user_id;