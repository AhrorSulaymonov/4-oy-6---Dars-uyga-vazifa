import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QPushButton

app = QApplication(sys.argv)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Radiobuttonlar yaratish
        self.radio_button_1 = QRadioButton('Option 1')
        self.radio_button_2 = QRadioButton('Option 2')
        self.radio_button_3 = QRadioButton('Option 3')

        # QButtonGroup orqali radiobuttonlarni birlashtirish
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)

        # Radiobuttonlarni tanlanmagan qilish uchun tugma
        self.clear_button = QPushButton('Clear Selection')
        self.clear_button.clicked.connect(self.clear_selection)

        # Layoutga qo'shish
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.radio_button_3)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

    def clear_selection(self):
        # Guruhdagi barcha radiobuttonlarni ajratib, tanlanmagan holatga qaytarish
        self.button_group.setExclusive(False)  # Radiobuttonlarni mustaqil qiladi
        for button in self.button_group.buttons():
            button.setChecked(False)
        self.button_group.setExclusive(True)  # Radiobuttonlarni qaytadan guruhlaydi

window = MyWindow()
window.show()
sys.exit(app.exec_())
