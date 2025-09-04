# Write your MySQL query statement below
select actor_id,director_id from (select actor_id,director_id,count(timestamp) as cnt from Actordirector group by actor_id,director_id) as t where cnt>=3;
