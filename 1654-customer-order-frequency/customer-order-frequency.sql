# Write your MySQL query statement below

with temp(customer_id,name,mnth,val) as (
select customer_id,name,mnth,sum(total) from 
(
select c.customer_id,c.name,month(o.order_date) as mnth,p.price*o.quantity as total from customers c left join orders o on c.customer_id=o.customer_id left join product p on o.product_id=p.product_id where year(o.order_date)='2020'
) as t where mnth=6 or mnth=7 group by customer_id,mnth
)

select c.customer_id,c.name from customers c left join temp t1 on c.customer_id=t1.customer_id left join temp t2 on c.customer_id=t2.customer_id where t1.mnth=6 and t2.mnth=7 and t1.val>=100 and t2.val>=100;