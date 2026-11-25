from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QFileDialog
import json
from pathlib import Path
from PyQt6.QtCore import Qt

def word_dict():
    search_word = text.text()
    path = Path("data.json")
    content = path.read_text()
    json_str_to_dict = json.loads(content)
    output_dict.setText(json_str_to_dict[search_word])


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
