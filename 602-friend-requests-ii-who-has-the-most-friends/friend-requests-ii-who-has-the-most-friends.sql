# Write your MySQL query statement below
select f1 as id,count(f2) as num from (select requester_id as f1,accepter_id as f2 from RequestAccepted
union all
select accepter_id as f1,requester_id as f2 from RequestAccepted) as t group by f1 order by num desc limit 1;