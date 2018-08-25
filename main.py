from qupu_reptile import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.setFixedSize(800,600);
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())