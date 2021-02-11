
import design
import tool
import TableCell
import Configuration

import sys

class Ui_MainWindowEvents(design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.fpl_tool = tool.Tool()
        self.config = Configuration.Configuration()


    def changeActivePage(self, page):
        self.scenes.setCurrentWidget(page)

        # difficulties might have been changed
        self.updateMyPlayersTable()
        self.setupFixturesTable()
    

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

        #changing difficulty
        new_difficulty = self.fpl_tool.teams.getTeamById(team_index).getDifficulty() + 1
        new_difficulty = ((new_difficulty - 1) % 5) + 1
        self.fpl_tool.teams.getTeamById(team_index).setDifficulty(new_difficulty)

        self.fpl_tool.teams.saveTeamDifficulties()

        self.showCurrentDifficulty(button, team_index)


    def setupChangeTeamsDifficulty(self):
        # adds onlick events to every team button
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
        self.showCurrentDifficulty(self.difficulty_button_9, 9) # leicester
        self.showCurrentDifficulty(self.difficulty_button_10, 10) # leeds

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


    def setupHoverButtons(self):
        list_of_buttons = [self.Planner, self.TeamDifficulty, self.Fixtures, self.Account, self.Quit, self.change_team_id_button, self.light_mode_button, self.dark_mode_button, self.add_player]

        for button in list_of_buttons:
            button.setStyleSheet("QPushButton::hover"
            "{"
                "background-color : "+ self.config.hover_menu_color +";"
            "}")

    def getCellText(self, opponents, i):
        opponent_team_name = ""
        number_of_fixtures = 0
        for opponent in opponents[i - 1]:
            if number_of_fixtures > 0:
                opponent_team_name += "+"

            opponent_team_name += self.fpl_tool.teams.getTeamById(opponent[0]).getAbb()
            opponent_team_name = opponent_team_name.upper()
            if opponent[1] == "H":
                opponent_team_name += "(H)"
            else:
                opponent_team_name += "(A)"

            number_of_fixtures += 1

        if len(opponents[i - 1]) == 0:
            opponent_team_name = "Blank"

        return opponent_team_name

    def addFixturesRowToTable(self, table, opponents, table_row):
        current_gameweek = self.fpl_tool.current_gameweek

        # gets opponents and information H/A
        for i in range (current_gameweek, 39):
            # creating button
            button = TableCell.TableCell()

            difficulty = 0

            # creating text
            opponent_team_name = self.getCellText(opponents, i)

            # number of fixtures and difficulty if double gameweek
            number_of_fixtures = 0
            for opponent in opponents[i - 1]:
                if number_of_fixtures > 0:
                    difficulty = -1
                number_of_fixtures += 1


            # change text
            button.setText(opponent_team_name)

            # changing color of a text
            #C button.setStyleSheet(button.styleSheet() + "color: " + self.config.font_color_string + ";\n")
            button.setFontColor(self.config.font_color_string)

            #changing background color of fixture
            if len(opponents[i - 1]) == 1:
                difficulty = self.fpl_tool.teams.getTeamById(opponents[i - 1][0][0]).getDifficulty()
            
            button.setDifficulty(difficulty)
            button.changeBackground(self.config) # based on difficulty

            # when clicked
            print(button.text())
            button.clicked.connect(lambda: self.changeCellVisibility(button))

            # updating style
            button.updateStyleSheet()

            # settling the button down
            self.my_players_table.setCellWidget(table_row - 1, i - current_gameweek + 1, button)


    def changeCellVisibility(self, button):
        new_button = self.sender()
        new_button.changeActivity(self.config)
        new_button.updateStyleSheet()


    def colorPlayer(self, row, column, player, table):
        position = player.getPosition()

        print("RC", row, column)

        if position == "Goalkeeper":
            table.item(row, column).setBackground(self.config.goalkeeper_color)
        if position == "Defender":
            table.item(row, column).setBackground(self.config.defender_color)
        if position == "Midfielder":
            table.item(row, column).setBackground(self.config.midfielder_color)
        if position == "Forward":
            table.item(row, column).setBackground(self.config.forward_color)

        # text color
        self.my_players_table.item(row, column).setForeground(self.config.font_color)


    def addPlayerToTable(self, player, table_id):
        # adding his name
        self.my_players_table.setItem(table_id - 1, 0, design.QtWidgets.QTableWidgetItem(player.name))
        self.colorPlayer(table_id - 1, 0, player, self.my_players_table)

        #adding fixtures
        current_gameweek = self.fpl_tool.current_gameweek
        # gets opponents and information H/A
        opponents = self.fpl_tool.teams.getTeamById(player.team_id).getOpponentsOfTeam()
        
        self.addFixturesRowToTable(self.my_players_table, opponents, table_id)


    def setupFrozenFixtures(self):
        teams = self.fpl_tool.teams.getTeams()

        table_row = 0
        self.frozen_fixtures.setRowCount(0)
        # add rows
        for team in teams:
            row_count = self.frozen_fixtures.rowCount()
            self.frozen_fixtures.setRowCount(row_count + 1)

        for team in teams:
            self.frozen_fixtures.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(team.getName()))
            table_row += 1


    def setupFrozenMyPlayers(self):
        players = self.fpl_tool.players_array

        table_row = 0
        self.frozen_my_players.setRowCount(0)

        # add rows
        for player in players:
            row_count = self.frozen_my_players.rowCount()
            self.frozen_my_players.setRowCount(row_count + 1)

        # adding goalkeepers
        number_of_goalkeepers = 0
        for player in self.fpl_tool.players_array:
            if player.position == "Goalkeeper":
                number_of_goalkeepers += 1
                self.frozen_my_players.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(player.getName()))
                self.frozen_my_players.setVerticalHeaderItem(table_row, design.QtWidgets.QTableWidgetItem("G" + str(number_of_goalkeepers)))
                self.colorPlayer(table_row, 0, player, self.frozen_my_players)
                self.frozen_my_players.item(table_row, 0).setFlags(design.QtCore.Qt.NoItemFlags)
                self.frozen_my_players.item(table_row, 0).setForeground(self.config.font_color)
                table_row += 1

        # adding defenders
        number_of_defenders = 0
        for player in self.fpl_tool.players_array:
            if player.position == "Defender":
                number_of_defenders += 1
                self.frozen_my_players.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(player.getName()))
                self.frozen_my_players.setVerticalHeaderItem(table_row, design.QtWidgets.QTableWidgetItem("D" + str(number_of_defenders)))
                self.colorPlayer(table_row, 0, player, self.frozen_my_players)
                self.frozen_my_players.item(table_row, 0).setFlags(design.QtCore.Qt.NoItemFlags)
                self.frozen_my_players.item(table_row, 0).setForeground(self.config.font_color)
                table_row += 1

        # adding midfielders
        number_of_midfielders = 0
        for player in self.fpl_tool.players_array:
            if player.position == "Midfielder":
                number_of_midfielders += 1
                self.frozen_my_players.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(player.getName()))
                self.frozen_my_players.setVerticalHeaderItem(table_row, design.QtWidgets.QTableWidgetItem("M" + str(number_of_midfielders)))
                self.colorPlayer(table_row, 0, player, self.frozen_my_players)
                self.frozen_my_players.item(table_row, 0).setFlags(design.QtCore.Qt.NoItemFlags)
                self.frozen_my_players.item(table_row, 0).setForeground(self.config.font_color)
                table_row += 1

        # adding forwards
        number_of_forwards = 0
        for player in self.fpl_tool.players_array:
            if player.position == "Forward":
                number_of_forwards += 1
                self.frozen_my_players.setItem(table_row, 0, design.QtWidgets.QTableWidgetItem(player.getName()))
                self.frozen_my_players.setVerticalHeaderItem(table_row, design.QtWidgets.QTableWidgetItem("F" + str(number_of_forwards)))
                self.colorPlayer(table_row, 0, player, self.frozen_my_players)
                self.frozen_my_players.item(table_row, 0).setFlags(design.QtCore.Qt.NoItemFlags)
                self.frozen_my_players.item(table_row, 0).setForeground(self.config.font_color)
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


    def addRowPT(self):
        row_count = self.my_players_table.rowCount()
        self.my_players_table.setRowCount(row_count + 1)


    def addTeamToTable(self, table_row, team):
        self.fixtures_table.setItem(table_row - 1, 0, design.QtWidgets.QTableWidgetItem(team.getName()))

        opponents = team.getOpponentsOfTeam()
        self.addFixturesRowToTable(self.fixtures_table, opponents, table_row)


    def setupFixturesTable(self):
        teams = self.fpl_tool.teams

        self.fixtures_table.setColumnCount(1)
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumnFT(i)

        self.fixtures_table.setRowCount(0)
        for team in teams.getTeams():
            #print(team.getName())
            self.addRowFT(team.getName())

        table_row = 1
        for team in teams.getTeams():
            #print(team.getName())
            self.addTeamToTable(table_row, team)

            table_row += 1


    def updateMyPlayersTable(self):
        self.my_players_table.setColumnCount(1)

        # adding columns
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumnPT(i)

        self.my_players_table.setRowCount(0)
        # adding rows for players
        for player in self.fpl_tool.players_array:
            self.addRowPT()

        print(self.fpl_tool.players_array)

        # adding players in correct order
        table_row = 1
        # adding goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Goalkeeper":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # adding defenders
        for player in self.fpl_tool.players_array:
            if player.position == "Defender":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # adding midfielders
        for player in self.fpl_tool.players_array:
            if player.position == "Midfielder":
                self.addPlayerToTable(player, table_row)
                table_row += 1

        # adding forwards
        for player in self.fpl_tool.players_array:
            if player.position == "Forward":
                self.addPlayerToTable(player, table_row)
                table_row += 1

    
    def setupSlider(self):
        self.gameweeks_slider.setMinimum(0)
        self.gameweeks_slider.setMaximum(38 - self.fpl_tool.current_gameweek)


    def quit(self):
        # terminates the PyQt
        design.QtWidgets.QApplication.quit()

        #terminates the program
        sys.exit()


    def setupSearchBox(self):
        full_names = []
        for player in self.fpl_tool.players.getPlayers():
            team = self.fpl_tool.teams.getTeamById(player.getTeamId())
            full_names.append(player.createCompleterString(team.getAbb()))

        # completer content
        completer = design.QtWidgets.QCompleter(full_names)

        #case sensitivity
        completer.setCaseSensitivity(design.QtCore.Qt.CaseInsensitive)

        # checks if string contains the pattern
        completer.setFilterMode(design.QtCore.Qt.MatchContains)

        self.search_box.setCompleter(completer)
        

    def changeMode(self, new_mode):
        if new_mode == "light":
            self.config.changeToDark()
        elif new_mode == "dark":
            self.config.changeToLight()
        self.updateEverything()


    def setupStyle(self):
        self.centralwidget.setStyleSheet(
        "QWidget#centralwidget {\n"
        "     background-image: url(\"C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png\")\n"
        "}\n"
        "\n"
        "\n"
        "QWidget QPushButton{ \n"
        "    background-color: " + self.config.button_background_color + ";\n"
        "    border-radius:10px;\n"
        "}\n"
        "\n"
        "QWidget {\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        ""
        )


    def addConceptPlayer(self):
        player_name = self.search_box.text()
        print(player_name)
        player = self.fpl_tool.players.getPlayerByCompleterString(player_name)

        self.fpl_tool.players_array.append(player)

        self.updateEverything()


    def setupOnclicks(self):
        # menu
        self.Planner.clicked.connect(lambda: self.changeActivePage(self.planner_page))
        self.TeamDifficulty.clicked.connect(lambda: self.changeActivePage(self.team_difficulty_page))
        self.Fixtures.clicked.connect(lambda: self.changeActivePage(self.fixtures_page))
        self.Account.clicked.connect(lambda: self.changeActivePage(self.account_page))
        self.Quit.clicked.connect(lambda: self.quit())

        # settings
        self.light_mode_button.clicked.connect(lambda: self.changeMode("light"))
        self.dark_mode_button.clicked.connect(lambda: self.changeMode("dark"))

        # add player (planner table)
        self.add_player.clicked.connect(lambda: self.addConceptPlayer())


    def updateEverything(self):
        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverButtons()

        self.updateMyPlayersTable()

        self.setupFixturesTable()

        self.setupFrozenFixtures()

        self.setupFrozenMyPlayers()


    def setupEvents(self):

        self.setupUi(self)

        self.setupStyle()

        # onlick functions for menu
        self.setupOnclicks()

        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverButtons()

        self.updateMyPlayersTable()

        self.setupSearchBox()

        self.setupFixturesTable()

        self.setupFrozenFixtures()

        self.setupFrozenMyPlayers()

        self.setupSlider()



        # background-image: url("C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png")
