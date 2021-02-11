
from PyQt5 import QtCore, QtGui, QtWidgets

class Configuration():
    black = QtGui.QColor(0, 0, 0)
    black_string = "#000000"
    white = QtGui.QColor(255, 255, 255)
    white_string = "#ffffff"


    double_gameweek_color = QtGui.QColor(255, 255, 70)
    difficulty0_color = QtGui.QColor(10, 10, 10)
    difficulty1_color = QtGui.QColor(0, 49, 29)
    difficulty2_color = QtGui.QColor(0, 99, 49)
    difficulty3_color = QtGui.QColor(91, 91, 91)
    difficulty4_color = QtGui.QColor(100, 9, 32)
    difficulty5_color = QtGui.QColor(50, 3, 18)

    double_gameweek_color_string = "#ffff46"
    difficulty0_color_string = "#0a0a0a"
    difficulty1_color_string = "#00311d"
    difficulty2_color_string = "#006331"
    difficulty3_color_string = "#5b5b5b"
    difficulty4_color_string = "#640920"
    difficulty5_color_string = "#320312"

    inactive_color_string = "#aaaaaa"


    goalkeeper_color = QtGui.QColor(92, 100, 0)
    defender_color = QtGui.QColor(0, 100, 53)
    midfielder_color = QtGui.QColor(2, 94, 100)
    forward_color = QtGui.QColor(91, 0, 32)

    hover_menu_color = "purple"


    mode = "light"
    font_color = QtGui.QColor(255, 255, 255)
    font_color_string = "#ffffff"
    main_background_color = "#505050"
    button_background_color = "#505050"


    def changeToDark(self):
        print("L")
        self.mode = "dark"
        self.font_color = QtGui.QColor(0, 0, 0)
        self.font_color_string = "#ffffff"
        self.main_background_color = "#ffffff"
        self.button_background_color = "#505050"

        
    def changeToLight(self):
        print("D")
        self.mode = "light"
        self.font_color = QtGui.QColor(255, 255, 255)
        self.font_color_string = "#000000"
        self.main_background_color = "#505050"
        self.button_background_color = "#ffffff"