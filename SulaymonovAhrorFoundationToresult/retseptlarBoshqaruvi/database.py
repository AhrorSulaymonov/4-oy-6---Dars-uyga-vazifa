import mysql.connector

class Database():
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )
        self.cursor = self.db.cursor()
        self._stamp()

    def _stamp(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS AhrorSulaymonov;")
        self.cursor.execute("USE  AhrorSulaymonov;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes(
                recipe_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                ingredients TEXT,
                instructions TEXT
            );
        """)

    def insert(self, name : str, ingredients : str, instructions : str):
        self.cursor.execute("INSERT INTO recipes values (NULL, %s, %s, %s);", (name, ingredients, instructions))
        self.db.commit()
    
    def selectByName(self, name):
        self.cursor.execute('select * from recipes where name = "' + name +'" ;')
        return self.cursor.fetchone()


    def names(self):
        self.cursor.execute("select name from recipes;")
        return self.cursor.fetchall()

    def searchwithingredients(self, ingredients : str):
        ingredientsList = ingredients.split()
        recieps = []
        for ingredient in ingredientsList:
            self.cursor.execute('Select name from recipes where ingredients like "%' + ingredient + '%" ;')
            recieps.append(self.cursor.fetchall())
        return recieps
    
    def searchwithinstructions(self, instructions : str):
        instructionsList = instructions.split()
        recieps = []
        for instructions in instructionsList:
            self.cursor.execute('Select name from recipes where instructions like "%' + instructions + '%" ;')
            recieps.append(self.cursor.fetchall())
        return recieps

    def update(self,recipe_id : int, name : str, ingredients : str, instructions : str):
        self.cursor.execute("""
            update recipes
            set name = %s,
                ingredients = %s,
                instructions = %s
            where recipe_id = %s;
        """,(name, ingredients, instructions, recipe_id))
        self.db.commit()
    
    def delete(self, recipe_id : int):
        self.cursor.execute("delete from recipes where recipe_id = " +str(recipe_id)+";")
        self.db.commit()


database = Database()


