# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyJaMa(object):
    def setupUi(self, PyJaMa):
        PyJaMa.setObjectName("PyJaMa")
        PyJaMa.resize(1103, 700)
        self.centralwidget = QtWidgets.QWidget(PyJaMa)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(460, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.PlainText)
        self.title.setObjectName("title")
        self.versionlabel = QtWidgets.QLabel(self.centralwidget)
        self.versionlabel.setGeometry(QtCore.QRect(460, 50, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.versionlabel.setFont(font)
        self.versionlabel.setTextFormat(QtCore.Qt.PlainText)
        self.versionlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionlabel.setObjectName("versionlabel")
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(520, 340, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.arrow.setFont(font)
        self.arrow.setTextFormat(QtCore.Qt.PlainText)
        self.arrow.setObjectName("arrow")
        self.result_validation = QtWidgets.QLabel(self.centralwidget)
        self.result_validation.setGeometry(QtCore.QRect(480, 240, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.result_validation.setFont(font)
        self.result_validation.setTextFormat(QtCore.Qt.PlainText)
        self.result_validation.setAlignment(QtCore.Qt.AlignCenter)
        self.result_validation.setObjectName("result_validation")
        self.validate_button = QtWidgets.QPushButton(self.centralwidget)
        self.validate_button.setGeometry(QtCore.QRect(500, 200, 101, 31))
        self.validate_button.setObjectName("validate_button")
        self.generate_label = QtWidgets.QLabel(self.centralwidget)
        self.generate_label.setGeometry(QtCore.QRect(480, 470, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.generate_label.setFont(font)
        self.generate_label.setTextFormat(QtCore.Qt.PlainText)
        self.generate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.generate_label.setObjectName("generate_label")
        self.generator_selector = QtWidgets.QComboBox(self.centralwidget)
        self.generator_selector.setGeometry(QtCore.QRect(490, 500, 121, 22))
        self.generator_selector.setObjectName("generator_selector")
        self.generator_selector.addItem("")
        self.generator_selector.addItem("")
        self.generator_button = QtWidgets.QPushButton(self.centralwidget)
        self.generator_button.setGeometry(QtCore.QRect(500, 540, 101, 31))
        self.generator_button.setObjectName("generator_button")
        self.validate_label = QtWidgets.QLabel(self.centralwidget)
        self.validate_label.setGeometry(QtCore.QRect(480, 160, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.validate_label.setFont(font)
        self.validate_label.setTextFormat(QtCore.Qt.PlainText)
        self.validate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.validate_label.setObjectName("validate_label")
        self.field_input = QtWidgets.QTextEdit(self.centralwidget)
        self.field_input.setGeometry(QtCore.QRect(10, 90, 441, 571))
        self.field_input.setObjectName("field_input")
        self.field_output = QtWidgets.QTextEdit(self.centralwidget)
        self.field_output.setGeometry(QtCore.QRect(650, 90, 441, 571))
        self.field_output.setObjectName("field_output")
        PyJaMa.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyJaMa)
        QtCore.QMetaObject.connectSlotsByName(PyJaMa)

    def retranslateUi(self, PyJaMa):
        _translate = QtCore.QCoreApplication.translate
        PyJaMa.setWindowTitle(_translate("PyJaMa", "PyJaMa"))
        self.title.setText(_translate("PyJaMa", "PyJaMa"))
        self.versionlabel.setText(_translate("PyJaMa", "v. 1.0 by Vittorio Picone"))
        self.arrow.setText(_translate("PyJaMa", "-->"))
        self.result_validation.setText(_translate("PyJaMa", "RESULT"))
        self.validate_button.setText(_translate("PyJaMa", "Validate JSON"))
        self.generate_label.setText(_translate("PyJaMa", "Generate:"))
        self.generator_selector.setItemText(0, _translate("PyJaMa", "Python Object"))
        self.generator_selector.setItemText(1, _translate("PyJaMa", "Flask API JSON Fetcher"))
        self.generator_button.setText(_translate("PyJaMa", "Generate"))
        self.validate_label.setText(_translate("PyJaMa", "Validate:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyJaMa = QtWidgets.QMainWindow()
    ui = Ui_PyJaMa()
    ui.setupUi(PyJaMa)
    PyJaMa.show()
    sys.exit(app.exec_())
