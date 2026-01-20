# Write your MySQL query statement below
with recursive t as (
    select task_id,subtasks_count from tasks
    union all
    select task_id,subtasks_count-1 from t
    where subtasks_count>1
)

select task_id,subtasks_count as subtask_id from t where (task_id,subtasks_count) not in (select * from executed);