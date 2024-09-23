from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLayout
from components import Label, Button, LineInput, TextInput

class InsertPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1000, 700)

        #id
        self.idLabel = Label("recipe_id", self)
        self.idInput = LineInput("id", self)
        self.idInput.setReadOnly(True)
        self.idLabel.move(50, 100)
        self.idInput.move(50, 150)

        #name
        self.nameLabel = Label("name", self)
        self.nameInput = LineInput("name", self)
        self.nameLabel.move(150, 100)
        self.nameInput.move(150, 150)

        #ingredients
        self.ingredientsLabel = Label("ingredients", self)
        self.ingredientsInput = TextInput("ingredients", self)
        self.ingredientsLabel.move(280, 100)
        self.ingredientsInput.move(280, 150)

        #instructions
        self.instructionsLabel = Label("instructions", self)
        self.instructionsInput = TextInput("instructions", self)
        self.instructionsLabel.move(530, 100)
        self.instructionsInput.move(530, 150)

        #insert
        self.insertBtn = Button("Insert", self)
        self.insertBtn.move(50, 500)

        #update
        self.updateBtn = Button("Update", self)
        self.updateBtn.move(200, 500)
       
        #delete
        self.deleteBtn = Button("Delete", self)
        self.deleteBtn.move(350, 500)

        #searchwithingredients
        self.searchwithingredientsBtn = Button("searchwithingredients",self)
        self.searchwithingredientsBtn.move(500, 500)

        #searchwithinstructions
        self.searchwithinstructionsBtn = Button("searchwithinstructions",self)
        self.searchwithinstructionsBtn.move(500, 500)



app = QApplication([])
oyna = InsertPage()
oyna.show()
app.exec()