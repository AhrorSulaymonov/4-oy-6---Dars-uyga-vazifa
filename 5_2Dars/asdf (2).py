from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QComboBox, QButtonGroup
from os import system

system("cls")
togricount = 0
TESTS = [
    {
        'id': 1,
        'question': "Tuxum birinchi paydo bo'lganmi tovuqmi?",
        'answers': {
            'A': "Tuxum",
            'B': "Tovuq",
            'C': "Aziz",
            'D': "Mo'rs"
        },
        'right_answer': ['C']
    },
    {
        'id': 2,
        'question': "O'zbekiston oldin nima deb nomlangan",
        'answers': {
            'A': "O'zbekiston",
            'B': "Qozog'iston",
            'C': "Qirg'iziston",
            'D': "Aziziston"
        },
        'right_answer': ['A']
    },
    {
        'id': 3,
        'question': "Ahror kim bo'lishni istidi",
        'answers': {
            'A': "Yaxshi odam",
            'B': "Repper",
            'C': "Yaxshi o'g'il",
            'D': "Milliarder"
        },
        'right_answer': ['A','B','C','D']
    },
    {
        'id': 4,
        'question': "Hayot to'la ...",
        'answers': {
            'A': "hazillar",
            'B': "va o'zgaradi manzillar",
            'C': "mashaqqatdan dars olib",
            'D': "men to'ldiraman puzllelar"
        },
        'right_answer': ['A','B','C','D']
    }
]

class Window(QWidget):
    last_question_index = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shunchaki")
        self.setFixedSize(800, 500)
        self.lastlabel = QLabel(self)
        
        self.lastlabel.move(200, 200)
        self.lastlabel.hide()
        self.questionLabel = QLabel("Savol", self)
        self.questionLabel.setStyleSheet("font-size: 22px; font-weight: bold; color: green;")
        self.questionLabel.move(20, 10)

        self.A_variant = QRadioButton("A", self)
        self.A_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.A_variant.move(50, 50)

        self.B_variant = QRadioButton("B", self)
        self.B_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.B_variant.move(50, 90)
        
        self.C_variant = QRadioButton("C", self)
        self.C_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.C_variant.move(50, 130)
        
        self.D_variant = QRadioButton("D", self)
        self.D_variant.setStyleSheet("font-size: 16px; color: #111336;")
        self.D_variant.move(50, 170)

        self.javoblar = QButtonGroup()
        self.javoblar.addButton(self.A_variant)
        self.javoblar.addButton(self.B_variant)
        self.javoblar.addButton(self.C_variant)
        self.javoblar.addButton(self.D_variant)

        self.nextBtn = QPushButton("Next", self)
        self.nextBtn.setStyleSheet("font-size: 20px;")
        self.nextBtn.move(600, 400)

        self.fillWindowWithQuestion()

        self.nextBtn.clicked.connect(self.nextFunction)

        self.show()
        

    def fillWindowWithQuestion(self):
        question = TESTS[self.last_question_index]

        self.questionLabel.setText(question['question'])
        self.A_variant.setText(question['answers']['A'])
        self.B_variant.setText(question['answers']['B'])
        self.C_variant.setText(question['answers']['C'])
        self.D_variant.setText(question['answers']['D'])

        self.A_variant.adjustSize()
        self.B_variant.adjustSize()
        self.C_variant.adjustSize()
        self.D_variant.adjustSize()
    def clearbuttons(self):
        self.javoblar.setExclusive(False)  # Radiobuttonlarni mustaqil qiladi
        for button in self.javoblar.buttons():
            button.setChecked(False)
        self.javoblar.setExclusive(True)  # Radiobuttonlarni qaytadan guruhlaydi

    def nextFunction(self):
        global togricount
        selected_button = self.javoblar.checkedButton()
        javoblartext = []
        if selected_button:
            for i in range(len(TESTS[self.last_question_index]["right_answer"])):
                javoblartext.append(TESTS[self.last_question_index]["answers"][TESTS[self.last_question_index]["right_answer"][i]])
            if selected_button.text() in javoblartext:
                togricount += 1
        self.clearbuttons()
        self.last_question_index += 1
        
        if self.last_question_index >= len(TESTS):
            self.A_variant.close()
            self.B_variant.close()
            self.C_variant.close()
            self.D_variant.close()
            self.questionLabel.clear()
            self.nextBtn.close()
            self.lastlabel.setText(f"Siz {togricount} ta tog'ri javob topdiz")
            self.lastlabel.show()
            
            print(f"{togricount}")
        else:
            self.fillWindowWithQuestion()
        


app = QApplication([])
oyna = Window()

app.exec()