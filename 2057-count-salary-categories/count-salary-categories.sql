# Write your MySQL query statement below
select t1.category,count(account_id) as accounts_count from (
select 'Low Salary' as category
union all
select 'Average Salary'as category
union all
select 'High Salary' as category) as t1 left join (select *,(case when income<20000 then 'Low Salary' when income between 20000 and 50000 then 'Average Salary' else 'High Salary' end) as category from Accounts) as t2 on t1.category=t2.category group by t1.category;