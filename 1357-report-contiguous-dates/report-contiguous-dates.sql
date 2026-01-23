# Write your MySQL query statement below
select * from (
select status as period_state,min(dt) as start_date,max(dt) as end_date from (
select *,date_sub(dt,interval rnk day) as diff from (
select *,rank() over(partition by status order by dt) as rnk from 
(select fail_date as dt,'failed' as status from Failed where year(fail_date)=2019
union all
select success_date as dr,'succeeded' as status from Succeeded where year(success_date)=2019) as t1) as t2) as t3 group by diff,status ) as t4 order by start_date