# PyQt6 English Dictionary

A desktop dictionary application built with **Python** and **PyQt6**. Users can type any English word into the graphical interface to instantly look up and display its definitions from a local JSON dataset.

## Features
* **Clean Desktop GUI:** Built with PyQt6 for fast, responsive local desktop usage.
* **Offline Word Lookup:** Searches a structured local JSON dictionary dataset with zero internet connection required.
* **Instant Definitions:** Displays single or multiple definitions clearly formatted for the user.

## Technologies Used
* **Python 3**
* **PyQt6** – Desktop Graphical User Interface (GUI)
* **JSON (`json` module)** – Parsing and querying the English dictionary dataset

## Project Structure
```text
PyQt6-English-Dictionary/
├── main.py              # Main PyQt6 application script
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
* Connecting Python data-lookup logic to a PyQt6 graphical interface using signals and slots.
* Reading and querying structured JSON files efficiently in Python.
* Packaging a local utility script into an interactive desktop application.
