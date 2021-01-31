import design
import tool

class Ui_MainWindowEvents(design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        print("D")
        self.fpl_tool = tool.Tool()


    def ChangeActivePage(self, page):
        self.scenes.setCurrentWidget(page)
        print("H")
    

    def ShowCurrentDifficulty(self, button, team_index):
        # updates text on a button
        difficulty = self.fpl_tool.team_difficulty[team_index - 1]
        if difficulty == 1:
            button.setText("very easy")
            button.setStyleSheet("background-color: green")
        if difficulty == 2:
            button.setText("easy")
            button.setStyleSheet("background-color: rgb(0, 99, 49)")
        if difficulty == 3:
            button.setText("medium")
            button.setStyleSheet("background-color: rgb(91, 91, 91)")
        if difficulty == 4:
            button.setText("hard")
            button.setStyleSheet("background-color: rgb(100, 9, 32)")
        if difficulty == 5:
            button.setText("very hard")
            button.setStyleSheet("background-color: rgb(50, 3, 18)")


    def ChangeTeamDifficulty(self, button, team_index):
        # called when button pressed
        print("C", button.objectName(), team_index)

        #changing array
        self.fpl_tool.team_difficulty[team_index - 1] += 1
        self.fpl_tool.team_difficulty[team_index - 1] = (self.fpl_tool.team_difficulty[team_index - 1] - 1) % 5 + 1

        print(self.fpl_tool.team_difficulty[team_index - 1])

        self.fpl_tool.saveTeamDifficulties()

        self.ShowCurrentDifficulty(button, team_index)


    def SetupChangeTeamsDifficulty(self):
        # # adds onlick events to every team button

        # print(len(design.QtWidgets.QPushButton.findChildren(self, design.QtWidgets.QPushButton)))
        
        # for i in range (1, 21):
        #     for team_button in design.QtWidgets.QPushButton.findChildren(self, design.QtWidgets.QPushButton):
        #     #loops through every button
        #         #checks name of a button and applies correct onlick function
        #         button_name = "difficulty_button_" + str(i)
        #         #print("STRING", button_name, team_button.objectName())
        #         if team_button.objectName() == button_name:
        #             print("TT", team_button.objectName(), i)
        #             team_button.clicked.connect(lambda: self.ChangeTeamDifficulty(team_button, i))
        
       
        self.difficulty_button_1.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_1, 1))
        self.difficulty_button_2.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_2, 2))
        self.difficulty_button_3.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_3, 3))
        self.difficulty_button_4.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_4, 4))
        self.difficulty_button_5.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_5, 5))

        self.difficulty_button_6.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_6, 6))
        self.difficulty_button_7.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_7, 7))
        self.difficulty_button_8.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_8, 8))
        self.difficulty_button_9.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_9, 9))
        self.difficulty_button_10.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_10, 10))

        self.difficulty_button_11.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_11, 11))
        self.difficulty_button_12.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_12, 12))
        self.difficulty_button_13.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_13, 13))
        self.difficulty_button_14.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_14, 14))
        self.difficulty_button_15.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_15, 15))

        self.difficulty_button_16.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_16, 16))
        self.difficulty_button_17.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_17, 17))
        self.difficulty_button_18.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_18, 18))
        self.difficulty_button_19.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_19, 19))
        self.difficulty_button_20.clicked.connect(lambda: self.ChangeTeamDifficulty(self.difficulty_button_20, 20))

        
    def showDifficulties(self):
        self.ShowCurrentDifficulty(self.difficulty_button_1, 1)
        self.ShowCurrentDifficulty(self.difficulty_button_2, 2)
        self.ShowCurrentDifficulty(self.difficulty_button_3, 3)
        self.ShowCurrentDifficulty(self.difficulty_button_4, 4)
        self.ShowCurrentDifficulty(self.difficulty_button_5, 5)

        self.ShowCurrentDifficulty(self.difficulty_button_6, 6)
        self.ShowCurrentDifficulty(self.difficulty_button_7, 7)
        self.ShowCurrentDifficulty(self.difficulty_button_8, 8)
        self.ShowCurrentDifficulty(self.difficulty_button_9, 9)
        self.ShowCurrentDifficulty(self.difficulty_button_10, 10)

        self.ShowCurrentDifficulty(self.difficulty_button_11, 11)
        self.ShowCurrentDifficulty(self.difficulty_button_12, 12)
        self.ShowCurrentDifficulty(self.difficulty_button_13, 13)
        self.ShowCurrentDifficulty(self.difficulty_button_14, 14)
        self.ShowCurrentDifficulty(self.difficulty_button_15, 15)

        self.ShowCurrentDifficulty(self.difficulty_button_16, 16)
        self.ShowCurrentDifficulty(self.difficulty_button_17, 17)
        self.ShowCurrentDifficulty(self.difficulty_button_18, 18)
        self.ShowCurrentDifficulty(self.difficulty_button_19, 19)
        self.ShowCurrentDifficulty(self.difficulty_button_20, 20)


    def SetupHoverMenu(self):
        list_of_menu = [self.Planner, self.TeamDifficulty]

        for menu_button in list_of_menu:
            menu_button.setStyleSheet("QPushButton::hover"
            "{"
                "background-color : purple;"
            "}")


    def setupEvents(self):
        print("U")

        self.fpl_tool.readTeamDifficulties()
        
        print(len(design.QtWidgets.QPushButton.findChildren(self, design.QtWidgets.QPushButton)))

        self.setupUi(self)

        self.TeamDifficulty.clicked.connect(lambda: self.ChangeActivePage(self.team_difficulty_page))
        self.Planner.clicked.connect(lambda: self.ChangeActivePage(self.planner_page))

        self.showDifficulties()

        self.SetupChangeTeamsDifficulty()

        self.SetupHoverMenu()

        print(len(design.QtWidgets.QPushButton.findChildren(self, design.QtWidgets.QPushButton)))

        #background-image: url("C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png")
