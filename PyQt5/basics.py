from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 400)
    win.setWindowTitle("Pehla GUI")

    label = QtWidgets.QLabel(win)
    label.setText("Pehla Label")
    label.move(200,50)


    win.show()
    sys.exit(app.exec_())

window()


