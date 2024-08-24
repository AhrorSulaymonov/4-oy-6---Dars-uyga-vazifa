from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QComboBox
from os import system

system("cls")

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
        'right_answer': 'C'
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
        'right_answer': 'A'
    },
]

class Window(QWidget):
    last_question_index = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bu mening 3-dasturim")
        self.setFixedSize(800, 500)

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

        self.nextBtn = QPushButton("Next", self)
        self.nextBtn.setStyleSheet("font-size: 20px;")
        self.nextBtn.move(600, 400)

        self.fillWindowWithQuestion()

        self.nextBtn.clicked.connect(self.nextFunction)

        self.show()
        

    def clearRadioButtons(self):
        self.A_variant.setChecked(False)
        self.B_variant.setChecked(False)
        self.C_variant.setChecked(False)
        self.D_variant.setChecked(False)


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


    def nextFunction(self):
        self.last_question_index += 1
        if self.last_question_index >= len(TESTS):
            print("Testlar tugadi")
        else:
            self.fillWindowWithQuestion()


app = QApplication([])
oyna = Window()

app.exec()