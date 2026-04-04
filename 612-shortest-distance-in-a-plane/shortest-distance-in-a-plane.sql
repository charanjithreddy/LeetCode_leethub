# Write your MySQL query statement below
select min(dist) as shortest from(
select round(sqrt(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2)),2) as dist from point2d p1 cross join point2d p2 on p1.x!=p2.x or p1.y!=p2.y) as t