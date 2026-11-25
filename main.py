from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QFileDialog
from PyQt6.QtCore import Qt

# def word_dict():


app =  QApplication([])
window = QWidget()
window.setWindowTitle("Word Dictionary/")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

output_dict = QLabel("")
layout.addWidget(output_dict)

btn = QPushButton("Meaning")
# btn.clicked.connect(word_dict)
layout.addWidget(btn)

window.setLayout(layout)
window.show()
app.exec()
