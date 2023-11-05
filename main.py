import sys
import json
from PyQt5 import Qsci
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt5.QtCore import Qt, QRegExp
from gui import Ui_PyJaMa

class JsonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(JsonSyntaxHighlighter, self).__init__(parent)
        self.json_format = QTextCharFormat()
        self.json_format.setForeground(Qt.darkBlue)
        self.json_format.setFontWeight(QFont.Bold)

        self.string_format = QTextCharFormat()
        self.string_format.setForeground(Qt.darkGreen)

        self.number_format = QTextCharFormat()
        self.number_format.setForeground(Qt.red)

    def highlightBlock(self, text):
        state = self.previousBlockState()
        startIndex = 0

        for i, char in enumerate(text):
            if state == 0:
                if char == '"':
                    if i == 0 or text[i - 1] != '\\':
                        startIndex = i
                        state = 1
                elif char in ('{', '}', '[', ']'):
                    self.setFormat(i, 1, self.json_format)
                elif char.isDigit() or char in ('-', '.', 'e', 'E'):
                    state = 2
            elif state == 1:  # Inside a string
                if char == '"' and text[i - 1] != '\\':
                    self.setFormat(startIndex, i - startIndex + 1, self.string_format)
                    state = 0
            elif state == 2:  # Inside a number
                if not (char.isDigit() or char in ('-', '.', 'e', 'E')):
                    self.setFormat(startIndex, i - startIndex, self.number_format)
                    state = 0

        self.setCurrentBlockState(state)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PyJaMa()  # Create an instance of the generated UI class

        self.ui.setupUi(self)  # Set up the UI
        Qsci.QsciLexerJSON(self.ui.field_input)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

