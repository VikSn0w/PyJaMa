import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt

class JSONHighlighter(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setPlainText('')
        self.setReadOnly(True)

    def highlight_json(self, json_text):
        self.setPlainText(json_text)

        cursor = QTextCursor(self.document())
        format = QTextCharFormat()
        cursor.movePosition(QTextCursor.Start)

        try:
            parsed_json = json.loads(json_text)
        except json.JSONDecodeError as e:
            # Handle invalid JSON input
            self.setStyleSheet("background-color: pink;")
            return

        for key, value in parsed_json.items():
            start_index = json_text.find(f'"{key}"')
            if start_index != -1:
                cursor.setPosition(start_index)
                cursor.setPosition(start_index + len(key) + 2, QTextCursor.KeepAnchor)
                format.setBackground(Qt.lightGray)
                cursor.setCharFormat(format)

    def clear_highlight(self):
        self.setStyleSheet("background-color: white;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSON Syntax Highlighter")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = JSONHighlighter()
        self.setCentralWidget(self.text_edit)

        example_json = '''{
            "name": "John",
            "age": 30,
            "city": "New York"
        }'''

        self.text_edit.highlight_json(example_json)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()