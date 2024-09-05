from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea

app = QApplication([])

# Scrollable area yaratish
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)

# Postlarni joylashtiradigan asosiy widget yaratish
posts_widget = QWidget()
posts_layout = QVBoxLayout(posts_widget)

# Bir nechta post qo'shish
for i in range(20):
    post = QLabel(f"Post #{i+1}")
    post.setStyleSheet("border: 1px solid black; padding: 10px; margin: 5px;")
    posts_layout.addWidget(post)

# Postlar joylashtirilgan widgetni scroll area ga qo'shish
scroll_area.setWidget(posts_widget)

# Asosiy oynani yaratish
main_window = QWidget()
main_layout = QVBoxLayout(main_window)
main_layout.addWidget(scroll_area)

main_window.setWindowTitle("Scrollable Posts Example")
main_window.resize(300, 400)
main_window.show()

app.exec_()
