
import design
import tool

import sys

class Ui_MainWindowEvents(design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        print("D")
        self.fpl_tool = tool.Tool()
        isQuit = False


    def changeActivePage(self, page):
        self.scenes.setCurrentWidget(page)
        print("H")
    

    def showCurrentDifficulty(self, button, team_index):
        # updates text on a button
        difficulty = self.fpl_tool.teams.getTeamById(team_index).getDifficulty()
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


    def changeTeamDifficulty(self, button, team_index):
        # called when button pressed
        print("C", button.objectName(), team_index)

        #changing difficulty
        new_difficulty = self.fpl_tool.teams.getTeamById(team_index).getDifficulty() + 1
        new_difficulty = ((new_difficulty - 1) % 5) + 1
        self.fpl_tool.teams.getTeamById(team_index).setDifficulty(new_difficulty)

        self.fpl_tool.teams.saveTeamDifficulties()

        self.showCurrentDifficulty(button, team_index)


    def setupChangeTeamsDifficulty(self):
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
        
       
        self.difficulty_button_1.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_1, 1))
        self.difficulty_button_2.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_2, 2))
        self.difficulty_button_3.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_3, 3))
        self.difficulty_button_4.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_4, 4))
        self.difficulty_button_5.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_5, 5))

        self.difficulty_button_6.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_6, 6))
        self.difficulty_button_7.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_7, 7))
        self.difficulty_button_8.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_8, 8))
        self.difficulty_button_9.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_9, 9))
        self.difficulty_button_10.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_10, 10))

        self.difficulty_button_11.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_11, 11))
        self.difficulty_button_12.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_12, 12))
        self.difficulty_button_13.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_13, 13))
        self.difficulty_button_14.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_14, 14))
        self.difficulty_button_15.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_15, 15))

        self.difficulty_button_16.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_16, 16))
        self.difficulty_button_17.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_17, 17))
        self.difficulty_button_18.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_18, 18))
        self.difficulty_button_19.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_19, 19))
        self.difficulty_button_20.clicked.connect(lambda: self.changeTeamDifficulty(self.difficulty_button_20, 20))

        
    def showDifficulties(self):
        self.showCurrentDifficulty(self.difficulty_button_1, 1)
        self.showCurrentDifficulty(self.difficulty_button_2, 2)
        self.showCurrentDifficulty(self.difficulty_button_3, 3)
        self.showCurrentDifficulty(self.difficulty_button_4, 4)
        self.showCurrentDifficulty(self.difficulty_button_5, 5)

        self.showCurrentDifficulty(self.difficulty_button_6, 6)
        self.showCurrentDifficulty(self.difficulty_button_7, 7)
        self.showCurrentDifficulty(self.difficulty_button_8, 8)
        self.showCurrentDifficulty(self.difficulty_button_9, 9)
        self.showCurrentDifficulty(self.difficulty_button_10, 10)

        self.showCurrentDifficulty(self.difficulty_button_11, 11)
        self.showCurrentDifficulty(self.difficulty_button_12, 12)
        self.showCurrentDifficulty(self.difficulty_button_13, 13)
        self.showCurrentDifficulty(self.difficulty_button_14, 14)
        self.showCurrentDifficulty(self.difficulty_button_15, 15)

        self.showCurrentDifficulty(self.difficulty_button_16, 16)
        self.showCurrentDifficulty(self.difficulty_button_17, 17)
        self.showCurrentDifficulty(self.difficulty_button_18, 18)
        self.showCurrentDifficulty(self.difficulty_button_19, 19)
        self.showCurrentDifficulty(self.difficulty_button_20, 20)


    def setupHoverMenu(self):
        list_of_menu = [self.Planner, self.TeamDifficulty, self.Quit]

        for menu_button in list_of_menu:
            menu_button.setStyleSheet("QPushButton::hover"
            "{"
                "background-color : purple;"
            "}")


    def addPlayerToTable(self, player, table_id):
        # adding his name
        self.my_players_table.setItem(table_id - 1, 0, design.QtWidgets.QTableWidgetItem(player.name))

        #adding fixtures
        current_gameweek = self.fpl_tool.current_gameweek
        opponents = self.fpl_tool.teams.getTeamById(player.team_id).getOpponentsOfTeam()
        for i in range (current_gameweek, 39):
            # setting text
            if opponents[i - 1] != 0:
                opponent_team_name = self.fpl_tool.teams.getTeamById(opponents[i - 1]).getName()
            else:
                opponent_team_name = "Blank"

            item = design.QtWidgets.QTableWidgetItem(opponent_team_name)
            item.setTextAlignment(design.QtCore.Qt.AlignCenter) # change the alignment
            self.my_players_table.setItem(table_id - 1, i - current_gameweek + 1, item)

            #changing color of fixture
            if opponents[i - 1] != 0:
                difficulty = self.fpl_tool.teams.getTeamById(opponents[i - 1]).getDifficulty()
            else:
                difficulty = 0
            
            if difficulty == 0:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(30, 30, 30))
            if difficulty == 1:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(0, 49, 29))
            if difficulty == 2:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(0, 99, 49))
            if difficulty == 3:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(91, 91, 91))
            if difficulty == 4:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(100, 9, 32))
            if difficulty == 5:
                self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(50, 3, 18))
                
            # changing color of a text
            self.my_players_table.item(table_id - 1, i - current_gameweek + 1).setForeground(design.QtGui.QColor(255, 255, 255))


    def addColumn(self, gameweek_number):
        column_count = self.my_players_table.columnCount()
        gameweek_string = "GW " + str(gameweek_number)
        self.my_players_table.setColumnCount(column_count + 1)
        self.my_players_table.setHorizontalHeaderItem(column_count, design.QtWidgets.QTableWidgetItem(gameweek_string))


    def updateMyPlayersTable(self):
        print("CG", self.fpl_tool.current_gameweek)
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumn(i)

        table_id = 1
        for player in self.fpl_tool.players_array:
            self.addPlayerToTable(player, table_id)
            table_id += 1

    
    def quit(self):
        # terminates the PyQt
        design.QtWidgets.QApplication.quit()

        #terminates the program
        sys.exit()

    def setupSearchBox(self):
        names = self.fpl_tool.players.getPlayersNames()
        completer = design.QtWidgets.QCompleter(names)
        self.search_box.setCompleter(completer)


    def setupEvents(self):
        print("U")

        
        print(len(design.QtWidgets.QPushButton.findChildren(self, design.QtWidgets.QPushButton)))

        self.setupUi(self)

        # onlick functions for menu
        self.Planner.clicked.connect(lambda: self.changeActivePage(self.planner_page))
        self.TeamDifficulty.clicked.connect(lambda: self.changeActivePage(self.team_difficulty_page))
        self.Quit.clicked.connect(lambda: self.quit())


        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverMenu()

        self.updateMyPlayersTable()

        self.setupSearchBox()


        #background-image: url("C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png")
