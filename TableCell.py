
from PyQt5 import QtWidgets

class TableCell(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
        self.border_radius = 0
        self.background_color = "#000000"
        self.font_color = "#ffffff"
        self.difficulty = 0
        self.active = True

        self.updateStyleSheet()

    def updateStyleSheet(self):
        self.setStyleSheet(
        "border-radius: 0px;\n"
        "background-color: " + self.background_color + ";\n"
        "color: " + self.font_color + ";\n"
        )
        
    def setFontColor(self, new_color):
        self.font_color = new_color

    def setBackgroundColor(self, new_color):
        self.background_color = new_color

    def setDifficulty(self, new_difficulty):
        self.difficulty = new_difficulty

    def changeBackground(self, config):
        if self.difficulty == -1:
            self.setBackgroundColor(config.double_gameweek_color_string)
            self.setFontColor(config.black_string)
        if self.difficulty == 0:
            self.setBackgroundColor(config.difficulty0_color_string)
            self.setFontColor(config.font_color_string)
        if self.difficulty == 1:
            self.setBackgroundColor(config.difficulty1_color_string)
            self.setFontColor(config.font_color_string)
        if self.difficulty == 2:
            self.setBackgroundColor(config.difficulty2_color_string)
            self.setFontColor(config.font_color_string)
        if self.difficulty == 3:
            self.setBackgroundColor(config.difficulty3_color_string)
            self.setFontColor(config.font_color_string)
        if self.difficulty == 4:
            self.setBackgroundColor(config.difficulty4_color_string)
            self.setFontColor(config.font_color_string)
        if self.difficulty == 5:
            self.setBackgroundColor(config.difficulty5_color_string)
            self.setFontColor(config.font_color_string)

    
    def changeActivity(self, config):
        if self.active:
            self.active = False
            self.setBackgroundColor(config.inactive_color_string)
        else:
            self.active = True
            self.changeBackground(config)