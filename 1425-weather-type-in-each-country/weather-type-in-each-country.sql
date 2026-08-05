# Write your MySQL query statement below
select country_name, case when avrg<=15 then "Cold" when avrg>=25 then "Hot" else "Warm" end as weather_type from ( 
select c.country_name,avg(w.weather_state) as avrg from countries c join weather w on c.country_id=w.country_id where month(w.day)=11 and year(w.day)=2019 group by c.country_name) as t