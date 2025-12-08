# Write your MySQL query statement below
select team_id,team_name,sum(points) as num_points from (

select t.team_id,t.team_name,ifnull(case when t.team_id=m1.host_team then (case when host_goals>guest_goals then 3 when host_goals=guest_goals then 1 else 0 end) when t.team_id=m1.guest_team then (case when guest_goals>host_goals then 3 when guest_goals=host_goals then 1 else 0 end ) end,0) as points from teams t left join matches m1 on t.team_id=m1.host_team or t.team_id=m1.guest_team) as temp group by team_id order by num_points desc,team_id asc;