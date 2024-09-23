select * from teachers order by salary ASC, experience DESC;

update teachers
set salary = salary - 1000
order by salary desc
limit 1;

select sum(monthly_payment * course_duration) from students;

update students
set branch = "dubay"
order by monthly_payment ASC, course_duration ASC
limit 1;

select t.name as teacher_name , t.surname as teacher_surname, s.name as student_name, s.surname as student_surname, t.branch
from teachers as t 
inner join students as s
on t.branch = s.branch;

