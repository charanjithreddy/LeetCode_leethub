# Write your MySQL query statement below
select *,
case when dna_sequence regexp '^ATG' then 1 else 0 end as has_start,
case when dna_sequence regexp 'TAA$' or dna_sequence regexp 'TAG$' or dna_sequence regexp 'TGA$' then 1 else 0 end as has_stop,
case when dna_sequence regexp 'ATAT' then 1 else 0 end as has_atat,
case when dna_sequence regexp 'GGG' then 1 else 0 end as has_ggg
from samples;