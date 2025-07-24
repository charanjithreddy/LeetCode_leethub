# Write your MySQL query statement below
select * from (select f1 as id,count(f2) as num from (select requester_id as f1,accepter_id as f2 from RequestAccepted
union all
select accepter_id as f1,requester_id as f2 from RequestAccepted) as t group by f1) as t1 
where num=(select max(num) from (select f1 as id,count(f2) as num from (select requester_id as f1,accepter_id as f2 from RequestAccepted
union all
select accepter_id as f1,requester_id as f2 from RequestAccepted) as t group by f1) as t2)