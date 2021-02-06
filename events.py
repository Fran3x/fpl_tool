
import design
import tool

import sys

class Ui_MainWindowEvents(design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.fpl_tool = tool.Tool()


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
        list_of_menu = [self.Planner, self.TeamDifficulty, self.Fixtures, self.Quit]

        for menu_button in list_of_menu:
            menu_button.setStyleSheet("QPushButton::hover"
            "{"
                "background-color : purple;"
            "}")


    def addFixturesRowToTable(self, table, opponents, table_row):
        current_gameweek = self.fpl_tool.current_gameweek

        difficulty = 0

        # gets opponents and information H/A
        for i in range (current_gameweek, 39):
            # setting text
            
            opponent_team_name = ""
            number_of_fixtures = 0
            for opponent in opponents[i - 1]:
                if number_of_fixtures > 0:
                    opponent_team_name += "+"
                    difficulty = -1

                opponent_team_name += self.fpl_tool.teams.getTeamById(opponent[0]).getAbb()
                opponent_team_name = opponent_team_name.upper()
                if opponent[1] == "H":
                    opponent_team_name += "(H)"
                else:
                    opponent_team_name += "(A)"

                number_of_fixtures += 1

            if len(opponents[i - 1]) == 0:
                opponent_team_name = "Blank"

            item = design.QtWidgets.QTableWidgetItem(opponent_team_name)
            item.setTextAlignment(design.QtCore.Qt.AlignCenter) # change the alignment
            table.setItem(table_row - 1, i - current_gameweek + 1, item)

            # changing color of a text
            table.item(table_row - 1, i - current_gameweek + 1).setForeground(design.QtGui.QColor(255, 255, 255))

            #changing background color of fixture
            if len(opponents[i - 1]) == 1:
                difficulty = self.fpl_tool.teams.getTeamById(opponent[0]).getDifficulty()
            
            if difficulty == -1:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(233, 233, 0))
                table.item(table_row - 1, i - current_gameweek + 1).setForeground(design.QtGui.QColor(0, 0, 0))
            if difficulty == 0:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(10, 10, 10))
            if difficulty == 1:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(0, 49, 29))
            if difficulty == 2:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(0, 99, 49))
            if difficulty == 3:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(91, 91, 91))
            if difficulty == 4:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(100, 9, 32))
            if difficulty == 5:
                table.item(table_row - 1, i - current_gameweek + 1).setBackground(design.QtGui.QColor(50, 3, 18))

            # not selectable
            table.item(table_row - 1, i - current_gameweek + 1).setFlags(design.QtCore.Qt.NoItemFlags)
                


    def colorPlayer(self, row, column, player):
        position = player.getPosition() 

        if position == "Goalkeeper":
            self.my_players_table.item(row, column).setBackground(design.QtGui.QColor(92, 100, 0))
        if position == "Defender":
            self.my_players_table.item(row, column).setBackground(design.QtGui.QColor(0, 100, 53))
        if position == "Midfielder":
            self.my_players_table.item(row, column).setBackground(design.QtGui.QColor(2, 94, 100))
        if position == "Forward":
            self.my_players_table.item(row, column).setBackground(design.QtGui.QColor(91, 0, 32))

        self.my_players_table.item(row, column).setForeground(design.QtGui.QColor(255, 255, 255))


    def addPlayerToTable(self, player, table_id):
        # adding his name
        self.my_players_table.setItem(table_id - 1, 0, design.QtWidgets.QTableWidgetItem(player.name))
        self.colorPlayer(table_id - 1, 0, player)

        #adding fixtures
        current_gameweek = self.fpl_tool.current_gameweek
        # gets opponents and information H/A
        opponents = self.fpl_tool.teams.getTeamById(player.team_id).getOpponentsOfTeam()
        
        self.addFixturesRowToTable(self.my_players_table, opponents, table_id)


    def setupFrozenFixtures(self):
        teams = self.fpl_tool.teams.getTeams()

        table_row = 0
        # add rows
        for team in teams:
            row_count = self.frozen_fixtures.rowCount()
            self.frozen_fixtures.setRowCount(row_count + 1)

        for team in teams:
            self.frozen_fixtures.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(team.getName()))
            table_row += 1


    def addColumnPT(self, gameweek_number):
        # PT - players table
        column_count = self.my_players_table.columnCount()
        gameweek_string = "GW " + str(gameweek_number)
        self.my_players_table.setColumnCount(column_count + 1)
        self.my_players_table.setHorizontalHeaderItem(column_count, design.QtWidgets.QTableWidgetItem(gameweek_string))


    def addColumnFT(self, gameweek_number):
        # FT - fixtures table
        column_count = self.fixtures_table.columnCount()
        gameweek_string = "GW " + str(gameweek_number)
        self.fixtures_table.setColumnCount(column_count + 1)
        self.fixtures_table.setHorizontalHeaderItem(column_count, design.QtWidgets.QTableWidgetItem(gameweek_string))


    def addRowFT(self, team_name):
        # FT - fixtures table
        row_count = self.fixtures_table.rowCount()
        self.fixtures_table.setRowCount(row_count + 1)

        # self.fixtures_table.setVerticalHeaderItem(row_count, design.QtWidgets.QTableWidgetItem(team_name))


    def addTeamToTable(self, table_row, team):
        self.fixtures_table.setItem(table_row - 1, 0, design.QtWidgets.QTableWidgetItem(team.getName()))

        opponents = team.getOpponentsOfTeam()
        self.addFixturesRowToTable(self.fixtures_table, opponents, table_row)


    def setupFixturesTable(self):
        teams = self.fpl_tool.teams

        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumnFT(i)

        for team in teams.getTeams():
            #print(team.getName())
            self.addRowFT(team.getName())

        table_row = 1
        for team in teams.getTeams():
            #print(team.getName())
            self.addTeamToTable(table_row, team)

            table_row += 1


    def updateMyPlayersTable(self):
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumnPT(i)

        # adding players in correct order
        table_row = 1
        # add goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Goalkeeper":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # add goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Defender":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # add goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Midfielder":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # add goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Forward":
                self.addPlayerToTable(player, table_row)
                table_row += 1

    
    def quit(self):
        # terminates the PyQt
        design.QtWidgets.QApplication.quit()

        #terminates the program
        sys.exit()


    def setupSearchBox(self):
        names = self.fpl_tool.players.getPlayersNames()
        completer = design.QtWidgets.QCompleter(names)
        self.search_box.setCompleter(completer)


    def setupOnclicks(self):
        self.Planner.clicked.connect(lambda: self.changeActivePage(self.planner_page))
        self.TeamDifficulty.clicked.connect(lambda: self.changeActivePage(self.team_difficulty_page))
        self.Fixtures.clicked.connect(lambda: self.changeActivePage(self.fixtures_page))
        self.Quit.clicked.connect(lambda: self.quit())


    def setupEvents(self):

        self.setupUi(self)

        # onlick functions for menu

        self.setupOnclicks()

        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverMenu()

        self.updateMyPlayersTable()

        self.setupSearchBox()

        self.setupFixturesTable()

        self.setupFrozenFixtures()


        #background-image: url("C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png")
