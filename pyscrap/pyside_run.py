"""

간단한 Python GUI 프로그램 

"""

import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<font color=purple size=40>검색어를 입력하세요!! >.o </font>")
label.show()
app.exec_()
print("Hello World")