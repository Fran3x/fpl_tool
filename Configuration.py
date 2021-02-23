
from PyQt5 import QtCore, QtGui, QtWidgets

class Configuration():
    def __init__(self):
        self.black = QtGui.QColor(0, 0, 0)
        self.black_string = "#000000"
        self.white = QtGui.QColor(255, 255, 255)
        self.white_string = "#ffffff"

        self.double_gameweek_color = QtGui.QColor(255, 255, 70)
        self.difficulty0_color = QtGui.QColor(10, 10, 10)
        self.difficulty1_color = QtGui.QColor(0, 49, 29)
        self.difficulty2_color = QtGui.QColor(0, 99, 49)
        self.difficulty3_color = QtGui.QColor(91, 91, 91)
        self.difficulty4_color = QtGui.QColor(100, 9, 32)
        self.difficulty5_color = QtGui.QColor(50, 3, 18)

        self.double_gameweek_color_string = "#ffff46"
        self.difficulty0_color_string = "#0a0a0a"
        self.difficulty1_color_string = "#00311d"
        self.difficulty2_color_string = "#006331"
        self.difficulty3_color_string = "#5b5b5b"
        self.difficulty4_color_string = "#640920"
        self.difficulty5_color_string = "#320312"

        self.inactive_color_string = "#bbbbbb"

        self.goalkeeper_color = QtGui.QColor(92, 100, 0)
        self.defender_color = QtGui.QColor(0, 100, 53)
        self.midfielder_color = QtGui.QColor(2, 94, 100)
        self.forward_color = QtGui.QColor(91, 0, 32)

        self.goalkeeper_color_string = "#5c6400"
        self.defender_color_string = "#006435"
        self.midfielder_color_string = "#025e64"
        self.forward_color_string = "#5b0020"

        self.hover_menu_color = "purple"

        self.mode = "light"
        self.font_color = QtGui.QColor(255, 255, 255)
        self.font_color_string = "#ffffff"
        self.main_background_color = "#bcbcbc"
        self.button_background_color = "#505050"

        self.premier_league_logo_path = "pics/logo_premier_league_small_black.png"


    def changeToDark(self):
        print("D")
        self.mode = "dark"
        self.font_color = QtGui.QColor(255, 255, 255)
        self.font_color_string = "#ffffff"
        self.main_background_color = "#505050"
        self.button_background_color = "#bcbcbc"
        self.premier_league_logo_path = "pics/logo_premier_league_small_white.png"

        
    def changeToLight(self):
        print("L")
        self.mode = "light"
        self.font_color = QtGui.QColor(255, 255, 255)
        self.font_color_string = "#ffffff"
        self.main_background_color = "#bcbcbc"
        self.button_background_color = "#505050"
        self.premier_league_logo_path = "pics/logo_premier_league_small_black.png"

    
    def changeToCustom(self):
        print("L")
        self.mode = "custom"
        self.font_color = QtGui.QColor(255, 255, 255)
        self.font_color_string = "#ffffff"
        self.button_background_color = "#505050"
        self.premier_league_logo_path = "pics/logo_premier_league_small_black.png"