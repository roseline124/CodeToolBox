""" 두개의 파이썬 파일을 불러와서 하나로 묶는 코드 """

import sys
from naverAPI_search import * #Crawler
from blog_cralwer import * #GUI


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    naverAPI_search.main()
    sys.exit(app.exec_())


