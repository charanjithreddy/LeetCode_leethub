# Write your MySQL query statement below
select customer_id,t1.product_id,product_name from (select customer_id,product_id,count(product_id) as cnt from orders group by customer_id,product_id) as t1 join products p on t1.product_id=p.product_id where (customer_id,cnt) in (
select customer_id,max(cnt) from (
select customer_id,product_id,count(product_id) as cnt from orders group by customer_id,product_id) as t group by customer_id)