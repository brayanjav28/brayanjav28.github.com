# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Generador.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest

import LogoU_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 531)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.apagadoboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.apagadoboton.setFont(font)
        self.apagadoboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.apagadoboton.setObjectName("apagadoboton")
        self.gridLayout_3.addWidget(self.apagadoboton, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(43)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3.addWidget(self.frame_3, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_3.addWidget(self.frame_8, 2, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.SR3 = QtWidgets.QPushButton(self.frame_6)
        self.SR3.setGeometry(QtCore.QRect(30, 70, 141, 23))
        self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR3.setText("")
        self.SR3.setObjectName("SR3")
        self.SA3 = QtWidgets.QPushButton(self.frame_6)
        self.SA3.setGeometry(QtCore.QRect(30, 40, 141, 23))
        self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA3.setText("")
        self.SA3.setObjectName("SA3")
        self.SV3 = QtWidgets.QPushButton(self.frame_6)
        self.SV3.setGeometry(QtCore.QRect(30, 10, 141, 23))
        self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV3.setText("")
        self.SV3.setObjectName("SV3")
        self.gridLayout_3.addWidget(self.frame_6, 3, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.SV1 = QtWidgets.QPushButton(self.frame_7)
        self.SV1.setGeometry(QtCore.QRect(30, 10, 141, 23))
        self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV1.setText("")
        self.SV1.setObjectName("SV1")
        self.SR1 = QtWidgets.QPushButton(self.frame_7)
        self.SR1.setGeometry(QtCore.QRect(30, 70, 141, 23))
        self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR1.setText("")
        self.SR1.setObjectName("SR1")
        self.SA1 = QtWidgets.QPushButton(self.frame_7)
        self.SA1.setGeometry(QtCore.QRect(30, 40, 141, 23))
        self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA1.setText("")
        self.SA1.setObjectName("SA1")
        self.gridLayout_3.addWidget(self.frame_7, 2, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.SR4 = QtWidgets.QPushButton(self.frame_9)
        self.SR4.setGeometry(QtCore.QRect(30, 70, 141, 23))
        self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR4.setText("")
        self.SR4.setObjectName("SR4")
        self.SA4 = QtWidgets.QPushButton(self.frame_9)
        self.SA4.setGeometry(QtCore.QRect(30, 40, 141, 23))
        self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA4.setText("")
        self.SA4.setObjectName("SA4")
        self.SV4 = QtWidgets.QPushButton(self.frame_9)
        self.SV4.setGeometry(QtCore.QRect(30, 10, 141, 23))
        self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV4.setText("")
        self.SV4.setObjectName("SV4")
        self.gridLayout_3.addWidget(self.frame_9, 2, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.SR2 = QtWidgets.QPushButton(self.frame_5)
        self.SR2.setGeometry(QtCore.QRect(30, 70, 141, 23))
        self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SR2.setText("")
        self.SR2.setObjectName("SR2")
        self.SV2 = QtWidgets.QPushButton(self.frame_5)
        self.SV2.setGeometry(QtCore.QRect(30, 10, 141, 23))
        self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SV2.setText("")
        self.SV2.setObjectName("SV2")
        self.SA2 = QtWidgets.QPushButton(self.frame_5)
        self.SA2.setGeometry(QtCore.QRect(30, 40, 141, 23))
        self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.SA2.setText("")
        self.SA2.setObjectName("SA2")
        self.gridLayout_3.addWidget(self.frame_5, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3.addWidget(self.frame_4, 3, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3.addWidget(self.frame_2, 1, 2, 1, 1)
        self.semiboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.semiboton.setFont(font)
        self.semiboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.semiboton.setObjectName("semiboton")
        self.gridLayout_3.addWidget(self.semiboton, 4, 2, 1, 1)
        self.manualboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.manualboton.setFont(font)
        self.manualboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.manualboton.setObjectName("manualboton")
        self.gridLayout_3.addWidget(self.manualboton, 4, 1, 1, 1)
        self.inicioboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.inicioboton.setFont(font)
        self.inicioboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.inicioboton.setObjectName("inicioboton")
        self.gridLayout_3.addWidget(self.inicioboton, 5, 0, 1, 1)
        self.autoboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.autoboton.setFont(font)
        self.autoboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.autoboton.setObjectName("autoboton")
        self.gridLayout_3.addWidget(self.autoboton, 5, 1, 1, 1)
        self.finalboton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.finalboton.setFont(font)
        self.finalboton.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.finalboton.setObjectName("finalboton")
        self.gridLayout_3.addWidget(self.finalboton, 5, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apagadoboton.setText(_translate("MainWindow", "APAGADO"))
        self.label.setText(_translate("MainWindow", "MANEJO DE SEMAFOROS"))
        self.semiboton.setText(_translate("MainWindow", "SEMI-AUTOMATICO"))
        self.manualboton.setText(_translate("MainWindow", "MANUAL"))
        self.inicioboton.setText(_translate("MainWindow", "VOLVER"))
        self.autoboton.setText(_translate("MainWindow", "AUTOMATICO"))
        self.finalboton.setText(_translate("MainWindow", "SIGUIENTE"))

        x=1

        while x==1:
            self.SV1.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR2.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.SV3.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR4.setStyleSheet("background-color: rgb(255, 0, 0);")
            QtTest.QTest.qWait(4000)
            self.SA1.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA2.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA3.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA4.setStyleSheet("background-color: rgb(255, 255, 0);")

            self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
            QtTest.QTest.qWait(2000)
            self.SV2.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.SA2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SA1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR1.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.SV4.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.SA4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SA3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR3.setStyleSheet("background-color: rgb(255, 0, 0);")
            QtTest.QTest.qWait(4000)
            self.SA1.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA2.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA3.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.SA4.setStyleSheet("background-color: rgb(255, 255, 0);")

            self.SV1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR1.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR2.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR3.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SV4.setStyleSheet("background-color: rgb(166, 166, 166);")
            self.SR4.setStyleSheet("background-color: rgb(166, 166, 166);")
            QtTest.QTest.qWait(2000)
            x=2



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())