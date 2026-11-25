from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton
import json
from pathlib import Path

def word_dict():
    search_word = text.text()
    search_word_low = search_word.lower()
    path = Path("data.json")
    content = path.read_text()
    json_str_to_dict = json.loads(content)
    if search_word_low in json_str_to_dict:
        output_dict.setText("\n".join(json_str_to_dict[search_word_low]))
    else:
        output_dict.setText("Sorry Word not Found")

app =  QApplication([])
window = QWidget()
window.setWindowTitle("Word Dictionary")

layout = QVBoxLayout()
layout.setContentsMargins(100, 100, 100, 100)
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
