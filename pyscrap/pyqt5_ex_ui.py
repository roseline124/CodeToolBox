# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_ex1_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqt5_ex1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #OK Button 
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(460, 80, 71, 28))
        self.okButton.setObjectName("okButton")

        #OK button Event 
        self.okButton.clicked.connect(self.okbtn_clicked)

        #lineEdit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 321, 41))
        self.lineEdit.setObjectName("lineEdit")

        #Window
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.okButton.setText(_translate("MainWindow", "OK"))

    def okbtn_clicked(self) :
        self.keyword = self.lineEdit.text()
    
        final_text = pyqt5_ex1.get_text(self.keyword) 
        self.lineEdit.setText(final_text + "입니다.") 

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()

#     #create instance 
#     ui = Ui_MainWindow()

#     #open window 
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

