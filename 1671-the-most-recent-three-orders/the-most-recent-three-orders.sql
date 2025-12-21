# Write your MySQL query statement below
select customer_name,customer_id,order_id,order_date from (
select c.name as customer_name,c.customer_id,o.order_id,o.order_date,row_number() over (partition by c.customer_id order by o.order_date desc) as rno from customers c inner join orders o on c.customer_id=o.customer_id) as temp where rno<=3 order by customer_name asc,customer_id asc,order_date desc