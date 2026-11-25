from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QFileDialog
from pathlib import Path
from PyQt6.QtCore import Qt

def word_dict():
    path = Path("data.json")
    for json in path:
        print(json)


app =  QApplication([])
window = QWidget()
window.setWindowTitle("Word Dictionary/")

layout = QVBoxLayout()
layout1 = QHBoxLayout()

layout.addLayout(layout1)

text = QLineEdit()
layout1.addWidget(text)

output_dict = QLabel("")
layout.addWidget(output_dict)

btn = QPushButton("Meaning")
btn.clicked.connect(word_dict)
layout1.addWidget(btn)

window.setLayout(layout)
window.show()
app.exec()
