"""
GUI 실행 
"""

import sys
from PyQt5.QtWidgets import *
# from PyQt5 import uic 

app = QApplication([])

dialog = QInputDialog()

dialog.show()

app.exec_()





# form_class = uic.loadUiType("blog_search.ui")[0]

# class Ui_Window(QMainWindow, form_class) :
#     def __init__(self) :
#         super().__init__()
#         self.setupUi(self)

# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     Ui_Window = Ui_Window()
#     Ui_Window.show()
#     app.exec_()
