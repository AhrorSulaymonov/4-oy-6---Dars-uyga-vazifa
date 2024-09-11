from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 400)
        
        # Create palette for background
        palette = QPalette()
        pixmap = QPixmap("Naruto.png")
        
        # Check if pixmap loaded successfully
        if not pixmap.isNull():
            palette.setBrush(QPalette.Background, QBrush(pixmap.scaled(self.size())))
            self.setPalette(palette)
        else:
            print("Rasmni yuklashda xatolik!")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec_()
