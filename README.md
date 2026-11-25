# PyQt6 English Dictionary

A lightweight desktop **Word Dictionary** application built with **Python** and **PyQt6**. Users can type any English word into the search bar, click **Meaning**, and immediately view its definitions pulled from a local `data.json` dataset.

## Features
* **Clean Desktop GUI:** Built with PyQt6 featuring a horizontal input bar (`QLineEdit` + **Meaning** button) and dynamic definition display (`QLabel`).
* **Offline Word Lookup:** Reads and queries a local `data.json` English dictionary file with zero internet connection required.
* **Case-Insensitive Search & Multi-Definition Formatting:** Automatically converts inputs to lowercase, displays multiple definitions cleanly line-by-line, and handles unknown words gracefully (`"Sorry Word not Found"`).

## Technologies Used
* **Python 3**
* **PyQt6** – Desktop Graphical User Interface (GUI)
* **JSON (`json` module)** – Parsing the English dictionary dataset
* **pathlib** – Clean, object-oriented file path reading

## Project Structure
```text
PyQt6-English-Dictionary/
├── main.py              # Main PyQt6 Word Dictionary script
├── data.json            # Local JSON dataset of English words and definitions
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd PyQt6-English-Dictionary
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## What I Learned
* Connecting user input (`QLineEdit`) and button click events (`QPushButton.clicked`) to Python lookup functions in PyQt6.
* Reading and parsing large JSON datasets using `pathlib` and `json.loads()`.
* Handling missing dictionary keys cleanly in a GUI environment.
