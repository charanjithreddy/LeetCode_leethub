
select player_id,player_name,sum(cnt) as grand_slams_count  from (
select player_id,player_name,count(year) as cnt from players join championships on player_id=wimbledon group by player_id
union all
select player_id,player_name,count(year) as cnt from players join championships on player_id=Fr_open group by player_id
union all
select player_id,player_name,count(year) as cnt from players join championships on player_id=Us_open group by player_id
union all
select player_id,player_name,count(year) as cnt from players join championships on player_id=Au_open group by player_id
)as t group by player_id