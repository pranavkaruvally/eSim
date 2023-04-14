# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBarNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Simulation(object):
    def setupUi(self, Simulation):
        Simulation.setObjectName("Simulation")
        Simulation.resize(1250, 652)
        self.progressBar = QtWidgets.QProgressBar(Simulation)
        self.progressBar.setGeometry(QtCore.QRect(27, 32, 660, 31))
        self.progressBar.setStyleSheet("")
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.simulationConsole = QtWidgets.QTextEdit(Simulation)
        self.simulationConsole.setGeometry(QtCore.QRect(30, 90, 661, 430))
        self.simulationConsole.setStyleSheet("")
        self.simulationConsole.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.simulationConsole.setObjectName("simulationConsole")
        self.pushButton = QtWidgets.QPushButton(Simulation)
        self.pushButton.setGeometry(QtCore.QRect(839, 330, 241, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Simulation)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 220, 240, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Simulation)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 430, 240, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Simulation)
        QtCore.QMetaObject.connectSlotsByName(Simulation)

    def retranslateUi(self, Simulation):
        _translate = QtCore.QCoreApplication.translate
        Simulation.setWindowTitle(_translate("Simulation", "Simulation"))
        self.simulationConsole.setHtml(_translate("Simulation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The quick brown fox jumped over the lazy dog</p></body></html>"))
        self.pushButton.setText(_translate("Simulation", "Button 2"))
        self.pushButton_2.setText(_translate("Simulation", "Cancel simulation"))
        self.pushButton_3.setText(_translate("Simulation", "Button 3"))

    def writeIntoConsole(self, consoleLog):    
        self.simulationConsole.insertPlainText(consoleLog)    
    
    def showProgressCompleted(self):    
        self.progressBar.setMaximum(100)    
        self.progressBar.setProperty("value", 100)