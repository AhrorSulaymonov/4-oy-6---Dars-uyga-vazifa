from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

# QListWidget yaratish
list_widget = QListWidget()

# Elementlar qo'shish
list_widget.addItem("Element 1")
list_widget.addItem("Element 2")

# Icon va matn bilan element qo'shish
item = QListWidgetItem("Element 3")
item.setIcon(QIcon('image.png'))  # Icon bilan ishlash
list_widget.addItem(item)

item = QListWidgetItem("Element 4")
item.setData(Qt.UserRole, "Qo'shimcha ma'lumot")  # Qo'shimcha ma'lumot o'rnatish
list_widget.addItem(item)

# Qo'shimcha ma'lumotni olish (element tanlanganda)
def on_item_selected():
    selected_item = list_widget.currentItem()
    print("Tanlangan element:", selected_item.text())
    
    # Qo'shimcha ma'lumotni olish
    extra_data = selected_item.data(Qt.UserRole)
    print("Qo'shimcha ma'lumot:", extra_data)

list_widget.itemClicked.connect(on_item_selected)

# Drag va drop rejimini o'rnatish
list_widget.setDragDropMode(QListWidget.InternalMove)

list_widget.show()

sys.exit(app.exec_())
