from main_body_GUI import *
import sys


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_new.clicked.connect(self.snc_text_label)

    def snc_text_label(self):
        self.l_display.setText("Новый расчёт!")
        self.l_display.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()

    sys.exit(app.exec())
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
