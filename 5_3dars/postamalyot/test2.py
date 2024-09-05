from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication([])

# Asosiy oyna yaratish
main_window = QWidget()

# QVBoxLayout yaratish (vertikal tartib)
v_layout = QVBoxLayout()

# QHBoxLayout yaratish (gorizontal tartib)
h_layout = QHBoxLayout()

# Tugmalar yaratish
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')

# Tugmalarni gorizontal layoutga qo'shish
h_layout.addWidget(button1)
h_layout.addWidget(button2)

# Gorizontal layoutni vertikal layoutga qo'shish
v_layout.addLayout(h_layout)

# Bitta tugmani vertikal layoutga qo'shish
v_layout.addWidget(button3)

# Layoutni asosiy oynaga qo'shish
main_window.setLayout(v_layout)

main_window.setWindowTitle("Layout Example")
main_window.show()

app.exec_()
