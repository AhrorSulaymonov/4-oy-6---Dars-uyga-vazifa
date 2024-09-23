import mysql.connector
from colorama import init, Fore
from os import system

system("cls")

init(autoreset=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2004"
)

kursor = db.cursor()

def createdatabase(DatabaseName : str):
    kursor.execute(f"CREATE DATABASE IF NOT EXISTS {DatabaseName};")
    print(Fore.GREEN + "* database yarratildi")

def connectdatabase(DatabaseName : str):
    kursor.execute(f"USE {DatabaseName};")
    print(Fore.GREEN + "* databasega ulandi")

def createtableteachers():
    kursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name varchar(50),
        surname varchar(50),
        salary int,
        experience int,
        branch varchar(50)               
    );
    """)
    print(Fore.GREEN + "* teachers table yaratildi")

def createtabletudents():
    kursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name varchar(50),
        surname varchar(50),
        monthly_payment int,
        course_duration int,
        branch varchar(50)               
    );
    """)
    print(Fore.GREEN + "* students table yaratildi")


def insertdatastudents(name : str,surname : str, monthly_payment : int, course_duration : int, branch : str):
    kursor.execute("insert into students (name, surname, monthly_payment, course_duration, branch) values (%s, %s, %s, %s, %s);",
    (name,surname,monthly_payment,course_duration,branch))
    db.commit()
    print(Fore.GREEN + "* 1ta ma'lumot qo'shildi")



def insertdatateachers(name : str,surname : str, salary : int, experience : int, branch : str):
    kursor.execute("insert into teachers (name, surname, salary, experience, branch) values (%s, %s, %s, %s, %s);",
    (name,surname,salary,experience,branch))
    db.commit()
    print(Fore.GREEN + "* 1ta ma'lumot qo'shildi")



createdatabase("School")
connectdatabase("School")
createtableteachers()
createtabletudents()
# insertdatateachers('Zachery', 'Petrichat', 228, 5, 'chilonzor')
# insertdatateachers('Emory', 'MacGinlay', 310, 5, 'xadra')
# insertdatateachers('Kaleb', 'Priest', 594, 5, 'chilonzor')
# insertdatateachers('Tojiddin','Helloyev', 142, 2, 'xadra')
# insertdatateachers('bo\'ri','wolkov', 652, 7, 'xadra')
# insertdatateachers('hwlo','hdhs', 542, 5, 'chilonzor')
# insertdatateachers('execute','ehhe', 1000, 9, 'chilonzor')
# insertdatateachers('Aziz','Azizov', 456, 4, 'farg\'ona')

# insertdatastudents("avazbek","primqulov",100,5,"chimboy")
# insertdatastudents('hello','helloyev',124,8,'chilonzor')
# insertdatastudents('miyasizxon','miyasizova',85,3,'bilmidi oziyam')
# insertdatastudents('maylida','kimdurov', 124, 7,'qayerdadur')
# insertdatastudents('helocha','hi gitler',114, 4,'mana yana kuz')
# insertdatastudents('barg','daraxtivosh',23,1,'yana yog\'ganda yomg\'ir')
# insertdatastudents('lo\'li','bosh kalla poycha', 54, 2, 'o\'rmon')

kursor.execute("select * from teachers order by salary;")
query1 = kursor.fetchall()

kursor.execute("select * from teachers order by salary ASC, experience DESC;")
query2 = kursor.fetchall()

kursor.execute("""update teachers
    set salary = salary - 1000
    order by salary desc
    limit 1;""")

kursor.execute("""update teachers
    set branch = "chilonzor"
    order by experience desc
    limit 1;""")

kursor.execute("select * from students order by surname;")
query5 = kursor.fetchall()

kursor.execute("select * from students order by monthly_payment DESC;")
query6 = kursor.fetchall()

kursor.execute("select sum(monthly_payment * course_duration) from students;")
query7 = kursor.fetchall()

kursor.execute("""update students
    set branch = "dubay"
    order by monthly_payment ASC, course_duration ASC
    limit 1;""")


kursor.execute("""select t.name as teacher_name , t.surname as teacher_surname, s.name as student_name, s.surname as student_surname, t.branch
    from teachers as t 
    inner join students as s
    on t.branch = s.branch;""")
query9 = kursor.fetchall()

kursor.execute("""select s1.name as firststudent_name, s2.name as secondstudent_name, s1.branch as firsts_branch, s2.branch as seconds_brinch
    from students as s1 
    inner join students as s2
    on s1.name = s2.name
    where s1.id <> s2.id;""")
query10 = kursor.fetchall()

kursor.execute("""select s1.surname as firststudent_surname, s2.surname as secondstudent_surname, s1.monthly_payment as firsts_monthly_payment, s2.monthly_payment as seconds_monthly_payment
    from students as s1 
    inner join students as s2
    on s1.surname = s2.surname
    where s1.id <> s2.id;""")
query10 = kursor.fetchall()

