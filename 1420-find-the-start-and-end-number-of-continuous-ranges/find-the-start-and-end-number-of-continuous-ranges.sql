# Write your MySQL query statement below
select min(log_id) as start_id,max(log_id) as end_id from(
select log_id,log_id-rnk as diff from(
select rank() over(order by log_id) as rnk,log_id from logs) as t) as t1 group by diff;