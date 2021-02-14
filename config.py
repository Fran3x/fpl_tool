
from PyQt5 import QtCore, QtGui, QtWidgets

class Configuration():
    black = QtGui.QColor(0, 0, 0)
    white = QtGui.QColor(255, 255, 255)

    double_gameweek_color = QtGui.QColor(255, 255, 70)
    difficulty0_color = QtGui.QColor(10, 10, 10)
    difficulty1_color = QtGui.QColor(0, 49, 29)
    difficulty2_color = QtGui.QColor(0, 99, 49)
    difficulty3_color = QtGui.QColor(91, 91, 91)
    difficulty4_color = QtGui.QColor(100, 9, 32)
    difficulty5_color = QtGui.QColor(50, 3, 18)

    goalkeeper_color = QtGui.QColor(92, 100, 0)
    defender_color = QtGui.QColor(0, 100, 53)
    midfielder_color = QtGui.QColor(2, 94, 100)
    forward_color = QtGui.QColor(91, 0, 32)

    hover_menu_color = "purple"


    mode = "light"
    font_color = QtGui.QColor(0, 0, 0)
    main_background_color = QtGui.QColor(50, 50, 50)
    button_background_color = QtGui.QColor(250, 250, 250)


    def changeToDark(self):
        print("L")
        mode = "dark"
        font_color = QtGui.QColor(255, 255, 255)
        main_background_color = QtGui.QColor(255, 255, 255)
        button_background_color = QtGui.QColor(50, 50, 50)

    def changeToLight(self):
        print("D")
        mode = "light"
        font_color = QtGui.QColor(0, 0, 0)
        main_background_color = QtGui.QColor(50, 50, 50)
        button_background_color = QtGui.QColor(250, 250, 250)