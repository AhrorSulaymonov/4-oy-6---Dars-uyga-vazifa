import mysql.connector

class Database():
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )

        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS shifoxona;")
        self.cursor.execute("USE shifoxona;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shifokorlar(
                id INT AUTO_INCREMENT PRIMARY KEY,
                ismi VARCHAR(50),
                familiyasi VARCHAR(50),
                mutaxasisligi VARCHAR(50),
                tajribasi INT,
                oyligi INT
            );""")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bemorlar(
                id INT AUTO_INCREMENT PRIMARY KEY,
                ismi VARCHAR(50),
                familiyasi VARCHAR(50),
                logini VARCHAR(50),
                paroli VARCHAR(50),
                kasallik_belgilari TEXT,
                joriy_shifokor_id INT 
            );""")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bemorlar(
                id INT AUTO_INCREMENT PRIMARY KEY,
                ismi VARCHAR(50),
                familiyasi VARCHAR(50),
                logini VARCHAR(50),
                paroli VARCHAR(50),
                kasallik_belgilari TEXT,
                joriy_shifokor_id INT 
            );""")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dorilar(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nomi VARCHAR(50),
                ishlabchiqarilgansanasi DATE,
                saqlash_muddati INT,
                narxi INT,
                dori_haqida TEXT
            );
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS uchrashuvlar(
            id INT AUTO_INCREMENT PRIMARY KEY,
            bemor_id INT,
            shifokor_id INT,
            uchrashuv_vaqti DATETIME
            );""")


        self.cursor.execute("select count(*) from shifokorlar;")
        shifokorlarsoni = self.cursor.fetchall()[0][0]
        if shifokorlarsoni == 0:
            self.cursor.execute("""
                insert into shifokorlar (ismi, familiyasi, mutaxasisligi, tajribasi, oyligi)
                values ('Artur', 'Nigmatov', 'psixolog', 25, 3000),
                        ('Olim', 'Shokirov', 'kardiolog', 7, 2000),
                        ('Sardor', 'Aliyev', 'lor', 5, 1000),
                        ('Aziza', 'Imronova', 'tish doktor', 8, 1200),
                        ('Abdulla', 'Azizov', 'Trambatolog', 7, 1200);
                """)
            self.db.commit()

database = Database()




