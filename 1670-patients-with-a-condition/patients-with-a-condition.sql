# Write your MySQL query statement below
select * from Patients where instr(conditions,"DIAB1")=1 or instr(conditions," DIAB1")!=0;