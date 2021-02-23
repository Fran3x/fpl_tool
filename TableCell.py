
from PyQt5 import QtWidgets

class TableCell(QtWidgets.QPushButton):
    def __init__(self, opponents=None):
        super().__init__()
        self.border_radius = 0
        self.background_color = "#000000"
        self.font_color = "#ffffff"
        if opponents == None: # only for fixtures cell
            self.opponents = None
        else:
            self.opponents = opponents
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


    def updateDifficulty(self, config, fpl_tool):
        # updates difficulty of a cell and then adjusts color
        #print("U")
        if len(self.opponents) > 1:
            self.difficulty = -1
        elif len(self.opponents) == 0:
            self.difficulty = 0
        else:
            self.difficulty = fpl_tool.teams.getTeamById(self.opponents[0][0]).getDifficulty()
            #print(self.difficulty)


    def changeBackground(self, config, fpl_tool):
        self.updateDifficulty(config, fpl_tool)
        if self.active == False:
            return
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
        # updates style
        self.updateStyleSheet()

    
    def changeActivity(self, config, fpl_tool):
        if self.active:
            self.changeToInactive(config)
        else:
            self.active = True
            self.changeBackground(config, fpl_tool)


    def changePlayerBackground(self, position, config):
        if position == "Goalkeeper":
            self.setBackgroundColor(config.goalkeeper_color_string)
        if position == "Defender":
            self.setBackgroundColor(config.defender_color_string)
        if position == "Midfielder":
            self.setBackgroundColor(config.midfielder_color_string)
        if position == "Forward":
            self.setBackgroundColor(config.forward_color_string)


    def changeToActive(self, config, fpl_tool):
        self.active = True
        self.changeBackground(config, fpl_tool)
        self.updateStyleSheet()


    def changeToInactive(self, config):
        self.active = False
        self.setBackgroundColor(config.inactive_color_string)
        self.setFontColor(config.black_string)
        self.updateStyleSheet()


    def isActive(self):
        return self.active
