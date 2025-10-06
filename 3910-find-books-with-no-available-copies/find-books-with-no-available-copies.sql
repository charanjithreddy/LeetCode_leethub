# Write your MySQL query statement below
select book_id,title,author,genre,publication_year, current_borrowers from (
select l.book_id,title,author,genre,publication_year,total_copies,count(b.record_id) as current_borrowers from library_books l left join borrowing_records b on l.book_id=b.book_id where  b.return_date is null group by b.book_id
) as t where current_borrowers=total_copies order by current_borrowers desc,title asc;