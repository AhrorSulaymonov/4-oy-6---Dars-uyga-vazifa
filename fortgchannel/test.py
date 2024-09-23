from PyQt5.QtWidgets import QApplication, QTextEdit

app = QApplication([])

# QTextEdit obyekti yaratamiz
text_edit = QTextEdit()
text_edit.setPlainText("Bu yerda matn bor!")

# Matnni olish uchun toPlainText() metodidan foydalanamiz
matn = text_edit.toPlainText()

print(matn)  # "Bu yerda matn bor!" ni chop etadi

text_edit.show()
app.exec_()
