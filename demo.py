# Form implementation generated from reading ui file 'D:\BitBreaker\demo.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 596)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BackGround = QtWidgets.QLabel(parent=self.centralwidget)
        self.BackGround.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.BackGround.setStyleSheet("background-image: url(:/newPrefix/demo background.png);")
        self.BackGround.setText("")
        self.BackGround.setObjectName("BackGround")
        self.Frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(500, 200, 361, 351))
        self.Frame.setStyleSheet("")
        self.Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame.setObjectName("Frame")
        self.label1 = QtWidgets.QLabel(parent=self.Frame)
        self.label1.setGeometry(QtCore.QRect(20, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setStyleSheet("text-colors: #f9e612;\n"
"border-image: url(:/newPrefix/bang.png);\n"
"color: rgb(249, 230, 18);\n"
"border-radius: 20px\n"
"")
        self.label1.setLineWidth(1)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label1.setObjectName("label1")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 160, 231, 31))
        self.lineEdit_2.setStyleSheet("    border: 2px solid #543927; /* Đổi màu và độ dày của border theo ý muốn */\n"
"    border-radius: 10px;\n"
"    background-color: rgb(247, 218, 158);\n"
"    font: 14pt \"ArcadeClassic\";\n"
"    text-align: center;\n"
"    padding: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.RunButton = QtWidgets.QPushButton(parent=self.Frame)
        self.RunButton.setGeometry(QtCore.QRect(40, 300, 81, 41))
        self.RunButton.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/newPrefix/run.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-image: url(:/newPrefix/run pressed.png);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    border-image: url(:/newPrefix/run.png);\n"
"\n"
"\n"
"}")
        self.RunButton.setText("")
        self.RunButton.setObjectName("RunButton")
        self.PauseButton = QtWidgets.QPushButton(parent=self.Frame)
        self.PauseButton.setGeometry(QtCore.QRect(240, 300, 81, 41))
        self.PauseButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    border-image: url(:/newPrefix/pause.png);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/newPrefix/pause pressed.png);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    border-image: url(:/newPrefix/pause.png);\n"
"\n"
"\n"
"}")
        self.PauseButton.setText("")
        self.PauseButton.setObjectName("PauseButton")
        self.label2 = QtWidgets.QLabel(parent=self.Frame)
        self.label2.setGeometry(QtCore.QRect(20, 110, 321, 51))
        font = QtGui.QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setStyleSheet("text-colors: #f9e612;\n"
"border-image: url(:/newPrefix/bang.png);\n"
"color: rgb(249, 230, 18);\n"
"")
        self.label2.setLineWidth(1)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(parent=self.Frame)
        self.label3.setGeometry(QtCore.QRect(20, 200, 321, 51))
        font = QtGui.QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setStyleSheet("text-colors: #f9e612;\n"
"border-image: url(:/newPrefix/bang.png);\n"
"color: rgb(249, 230, 18);\n"
"")
        self.label3.setLineWidth(1)
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.Frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 250, 231, 31))
        self.lineEdit.setStyleSheet("    border: 2px solid #543927; /* Đổi màu và độ dày của border theo ý muốn */\n"
"    border-radius: 10px;\n"
"    background-color: rgb(247, 218, 158);\n"
"    font: 14pt \"ArcadeClassic\";\n"
"    text-align: center;\n"
"    padding: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=self.Frame)
        self.comboBox.setGeometry(QtCore.QRect(70, 70, 231, 31))
        font = QtGui.QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("    border: 2px solid #543927; /* Đổi màu và độ dày của border theo ý muốn */\n"
"    border-radius: 10px;\n"
"    background-color: rgb(247, 218, 158);\n"
"    font: 14pt \"ArcadeClassic\";\n"
"    text-align: center;\n"
"    padding: 5px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(90, 210, 210, 36))
        font = QtGui.QFont()
        font.setFamily("ArcadeClassic")
        font.setPointSize(16)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setObjectName("label4")
        self.Volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.Volume.setGeometry(QtCore.QRect(0, 0, 91, 41))
        self.Volume.setStyleSheet("")
        self.Volume.setText("")
        self.Volume.setObjectName("Volume")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 10, 41, 22))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: #b0b0b0;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #f9e610; /* Màu đỏ cho handle */\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* Move handle up and down */\n"
"    border-radius: 3px;\n"
"}\n"
"color: rgb(249, 230, 16);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.SpeakerIcon = QtWidgets.QLabel(parent=self.centralwidget)
        self.SpeakerIcon.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.SpeakerIcon.setStyleSheet("border-image: url(:/newPrefix/465242.png);")
        self.SpeakerIcon.setText("")
        self.SpeakerIcon.setObjectName("SpeakerIcon")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.label3.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dat"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hoan"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Trung"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Duong"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Viet"))
        self.label4.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())