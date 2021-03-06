
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

import events
import tool

# "QWidget#centralwidget {\n"
#         "     background-image: url(\"C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png\")\n"
#         "}\n"


#cd C:\Users\Franex\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\PySide2\fpl_tool && pyuic5 -x design.ui -o design.py
#cd C:\Users\Franex\Desktop\fpl_tool && pyuic5 -x design.ui -o design.py

class App(QtWidgets.QMainWindow, events.Ui_MainWindowEvents):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupEvents()


if __name__ == "__main__":
    new_app = QApplication(sys.argv)
    form = App()
    form.setWindowIcon(QtGui.QIcon('pics/shortcut_pic.ico'))
    form.setWindowTitle('FPL Tool')
    form.show()
    new_app.exec_()
