from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QListWidget
from components import Label, Button, LineInput, TextInput
from database import database
class InsertPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1000, 700)

        #id
        self.idLabel = Label("recipe_id", self)
        self.idInput = LineInput("id", self)
        self.idInput.setReadOnly(True)
        self.idLabel.move(50, 50)
        self.idInput.move(50, 100)

        #name
        self.nameLabel = Label("name", self)
        self.nameInput = LineInput("name", self)
        self.nameLabel.move(150, 50)
        self.nameInput.move(150, 100)

        #ingredients
        self.ingredientsLabel = Label("ingredients", self)
        self.ingredientsInput = TextInput("ingredients", self)
        self.ingredientsLabel.move(280, 50)
        self.ingredientsInput.move(280, 100)

        #instructions
        self.instructionsLabel = Label("instructions", self)
        self.instructionsInput = TextInput("instructions", self)
        self.instructionsLabel.move(530, 50)
        self.instructionsInput.move(530, 100)

        #insert
        self.insertBtn = Button("Insert", self)
        self.insertBtn.move(50, 600)
        self.insertBtn.clicked.connect(self.insert)

        #update
        self.updateBtn = Button("Update", self)
        self.updateBtn.move(200, 600)
        self.updateBtn.clicked.connect(self.update)

        #delete
        self.deleteBtn = Button("Delete", self)
        self.deleteBtn.move(350, 600)
        self.deleteBtn.clicked.connect(self.delete)

        #searchwithingredients
        self.searchwithingredientsBtn = Button("searchwithingredients",self)
        self.searchwithingredientsBtn.move(500, 600)
        self.searchwithingredientsBtn.clicked.connect(self.searchwithingredients)
        #searchwithinstructions
        self.searchwithinstructionsBtn = Button("searchwithinstructions",self)
        self.searchwithinstructionsBtn.move(650, 600)
        self.searchwithinstructionsBtn.clicked.connect(self.searchwithinstructions)

        #retseptnomi uchun listwidget
        self.nameRecipeListLabel = Label("Retseptlar",self)
        self.nameRecipeList = QListWidget(self)
        self.nameRecipeListLabel.move(200, 320)
        self.nameRecipeList.move(200,350)
        self.fillNameRecipeList()
        self.nameRecipeList.itemClicked.connect(self.nameRecipeListClicked)


        #clear Button qo'shamiz
        self.clearBtn = Button("Clear", self)
        self.clearBtn.move(800, 500)
        self.clearBtn.clicked.connect(self.clear)


    def clear(self):
        self.nameInput.setText("")
        self.ingredientsInput.setText("")
        self.instructionsInput.setText("")
        self.idInput.setText("")
        self.nameRecipeList.clear()
        self.fillNameRecipeList()

    def fillNameRecipeList(self):
        names = database.names()
        for name in names:
            self.nameRecipeList.addItem(name[0])

    def nameRecipeListClicked(self):
        name = self.nameRecipeList.currentItem().text()
        aboutRecipe = database.selectByName(name)
        self.idInput.setText(str(aboutRecipe[0]))
        self.nameInput.setText(aboutRecipe[1])
        self.ingredientsInput.setPlainText(aboutRecipe[2])
        self.instructionsInput.setPlainText(aboutRecipe[3])

    def insert(self):
        name = self.nameInput.text()
        ingredients = self.ingredientsInput.toPlainText()
        instructions = self.instructionsInput.toPlainText()
        database.insert(name, ingredients, instructions)
        self.nameRecipeList.clear()
        self.fillNameRecipeList()

        self.nameInput.setText("")
        self.ingredientsInput.setText("")
        self.instructionsInput.setText("")

    def searchwithingredients(self):
        ingredients = self.ingredientsInput.toPlainText()
        recieps = database.searchwithingredients(ingredients)
        self.nameRecipeList.clear()
        for reciep in recieps:
            self.nameRecipeList.addItem(reciep[0][0])
    
    def searchwithinstructions(self):
        instructions = self.instructionsInput.toPlainText()
        recieps = database.searchwithinstructions(instructions)
        self.nameRecipeList.clear()
        if len(recieps) >= 1 and len(recieps[0]) >= 1:
            for reciep in recieps:
                self.nameRecipeList.addItem(reciep[0][0])
    
    def update(self):
        recipe_id = self.idInput.text()
        name = self.nameInput.text()
        ingredients = self.ingredientsInput.toPlainText()
        instructions = self.instructionsInput.toPlainText()

        database.update(recipe_id, name, ingredients, instructions)
        self.nameInput.setText("")
        self.ingredientsInput.setText("")
        self.instructionsInput.setText("")
        self.idInput.setText("")
        self.nameRecipeList.clear()
        self.fillNameRecipeList()
    
    def delete(self):
        recipe_id = self.idInput.text()
        database.delete(recipe_id)
        self.nameInput.setText("")
        self.ingredientsInput.setText("")
        self.instructionsInput.setText("")
        self.idInput.setText("")
        self.nameRecipeList.clear()
        self.fillNameRecipeList()




app = QApplication([])
oyna = InsertPage()
oyna.show()
app.exec()
