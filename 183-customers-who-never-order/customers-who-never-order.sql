# Write your MySQL query statement below
select name as customers from (select c.id,c.name,o.customerId from customers c left join orders o on c.id=o.customerId having o.customerId is null) as t;