"""
main program 
"""

import sys
from pyqt5_ex1_ui import * 

#get text and print 


def get_text(text) : 
    print("ui로부터" + text + "를 전달 받음")
    text = text*2 
    return text 
    # toss text 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #create instance 
    ui = Ui_MainWindow()

    #open window 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())