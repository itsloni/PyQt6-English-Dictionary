from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QFileDialog
from PyQt6.QtCore import Qt

app =  QApplication([])
window = QWidget()
window.setWindowTitle("Word Dictionary/")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

output_dict = QLabel("")
layout.addWidget(output_dict)


window.setLayout(layout)
window.show()
app.exec()
