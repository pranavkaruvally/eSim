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
        self.progressBar.setGeometry(QtCore.QRect(27, 310, 1191, 31))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(38, 162, 105);\n"
"}")
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Simulation)
        QtCore.QMetaObject.connectSlotsByName(Simulation)

    def retranslateUi(self, Simulation):
        _translate = QtCore.QCoreApplication.translate
        Simulation.setWindowTitle(_translate("Simulation", "Simulation"))

    def makeProgressComplete(self):
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 100)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simulation = QtWidgets.QWidget()
    ui = Ui_Simulation()
    ui.setupUi(Simulation)
    Simulation.show()
    sys.exit(app.exec_())
