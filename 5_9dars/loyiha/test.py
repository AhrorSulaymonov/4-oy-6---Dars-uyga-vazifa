from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QLabel

class ComboBoxReactionDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ComboBox Signal Example")
        layout = QVBoxLayout()
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.combo_box)
        
        # Natijalarni ko'rsatish uchun Label
        self.label = QLabel("Tanlovingizni bu yerda ko'rasiz.")
        layout.addWidget(self.label)
        
        # currentIndexChanged signalini ulaymiz
        self.combo_box.currentIndexChanged.connect(self.combo_changed)
        
        self.setLayout(layout)
        
    def combo_changed(self, index):
        # Tanlangan element o'zgarishi bilan bu funksiya chaqiriladi
        selected_text = self.combo_box.currentText()  # Tanlangan matn
        self.label.setText(f"Tanlangan: {selected_text}")

app = QApplication([])
window = ComboBoxReactionDemo()
window.show()
app.exec_()
