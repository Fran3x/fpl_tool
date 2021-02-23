
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


    def addColumn(self, table, gameweek_number = None):
        column_count = table.columnCount()
        table.setColumnCount(column_count + 1)
        if table == self.fixtures_table or table == self.my_players_table:
            gameweek_string = "GW " + str(gameweek_number)
            table.setHorizontalHeaderItem(column_count, design.QtWidgets.QTableWidgetItem(gameweek_string))


    def addConceptPlayer(self):
        player_name = self.search_box.text()
        #print(player_name)
        if player_name == "":
            print("Enter player name first")
            return
        player = self.fpl_tool.players.getPlayerByCompleterString(player_name)

        if player == None:
            print("No such player found")
            return
        elif player in self.fpl_tool.players_array:
            print("Player already added")
            return
        else:
            self.addConceptToMyPlayers(player)
            self.setupFrozenMyPlayers()

        #self.updateTable(self.my_players_table)


    def addConceptToMyPlayers(self, player):
        self.fpl_tool.players_array.append(player)
        # inserting a row to players table for ne player
        row = self.calculateRowNumber(player)
        self.my_players_table.insertRow(row)
        # adding to table
        self.addPlayerToTable(player, row + 1)


    def addFixturesRowToTable(self, table, opponents, table_row):
        current_gameweek = self.fpl_tool.current_gameweek

        # gets opponents and information H/A
        for i in range (current_gameweek, 39):
            # creating button
            button = TableCell.TableCell(opponents[i - 1])

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
            button.changeBackground(self.config, self.fpl_tool) # based on difficulty

            # onclick event
            if table != self.fixtures_table:
                button.clicked.connect(lambda: self.changeCellVisibility(button))

            # updating style
            button.updateStyleSheet()

            # settling the button down
            table.setCellWidget(table_row - 1, i - current_gameweek + 1, button)

            # not clickable if fixtures table
            # if table == self.fixtures_table:
                # table.itemAt(table_row - 1, i - current_gameweek + 1).setFlags(design.QtCore.Qt.NoItemFlags)


    def addPlayerToTable(self, player, table_id):
        # gets opponents and information H/A
        opponents = self.fpl_tool.teams.getTeamById(player.team_id).getOpponentsOfTeam()
        
        self.addFixturesRowToTable(self.my_players_table, opponents, table_id)


    def addRow(self, table):
        row_count = table.rowCount()
        table.setRowCount(row_count + 1)



    def addTeamToTable(self, table_row, team):
        self.fixtures_table.setItem(table_row - 1, 0, design.QtWidgets.QTableWidgetItem(team.getName()))

        opponents = team.getOpponentsOfTeam()
        self.addFixturesRowToTable(self.fixtures_table, opponents, table_row)


    def calculateActivePlayersColumn(self, column):
        row = 0
        number_of_active = 0
        for player in self.fpl_tool.players_array:
            button = self.my_players_table.cellWidget(row, column)
            if button.isActive():
                number_of_active += 1
            row += 1
        return number_of_active


    def calculateRowNumber(self, new_player):
        table_row = 0
        # adding goalkeepers
        for player in self.fpl_tool.players_array:
            if player.position == "Goalkeeper":
                if player == new_player:
                    return table_row
                table_row += 1

        # adding defenders
        for player in self.fpl_tool.players_array:
            if player.position == "Defender":
                if player == new_player:
                    return table_row
                table_row += 1

        # adding midfielders
        for player in self.fpl_tool.players_array:
            if player.position == "Midfielder":
                if player == new_player:
                    return table_row
                table_row += 1

        # adding forwards
        for player in self.fpl_tool.players_array:
            if player.position == "Forward":
                if player == new_player:
                    return table_row
                table_row += 1
        
        return None


    def changeActivePage(self, page):
        self.scenes.setCurrentWidget(page)

        # difficulties might have changed
        self.updateBackgroundColors


    def changeAllToActive(self, config):
        rows = self.my_players_table.rowCount()
        columns = self.my_players_table.columnCount()

        # activate every cell
        for j in range (1, columns):
            for i in range (0, rows):
                self.my_players_table.cellWidget(i, j).changeToActive(config, self.fpl_tool)

        # refresh active players table
        self.setupActivePlayersTable()


    def changeCellVisibility(self, button):
        new_button = self.sender()
        new_button.changeActivity(self.config, self.fpl_tool)
        self.setupActivePlayersTable()


    def changeMode(self, new_mode):
        if new_mode == "light":
            self.config.changeToLight()
        elif new_mode == "dark":
            self.config.changeToDark()
        elif new_mode == "custom":
            self.config.changeToCustom()
        self.setupStyle()


    def changePlayerActivity(self, config):
        # changes status of all fixtures of clicked player
        position = self.frozen_my_players.indexAt(self.sender().pos())
        row = position.row()
        current_gameweek = self.fpl_tool.current_gameweek
        for i in range (current_gameweek, 39):
            column = i - current_gameweek + 1
            button = self.my_players_table.cellWidget(row, column)
            button.changeToInactive(self.config)
        self.setupActivePlayersTable()


    def changeTeamDifficulty(self, button, team_index):
        # called when button pressed

        # changing difficulty of Team object
        new_difficulty = self.fpl_tool.teams.getTeamById(team_index).getDifficulty() + 1
        new_difficulty = ((new_difficulty - 1) % 5) + 1
        self.fpl_tool.teams.getTeamById(team_index).setDifficulty(new_difficulty)

        # saving to file
        self.fpl_tool.teams.saveTeamDifficulties()

        # showing correct color on team difficulty page
        self.showCurrentDifficulty(button, team_index)

        # correct color on other pages
        self.updateTables()


    def changeTeamId(self):
        new_id = int(self.team_id_box.toPlainText())
        print(new_id)
        self.fpl_tool.setTeamId(new_id)
        self.updateForNewTeam()


    def updateForNewTeam(self):
        self.fpl_tool.getPlayersIds()
        self.fpl_tool.getPlayersIds()
        self.fpl_tool.getPlayersNames()
        
        print(self.fpl_tool.players_array)
        self.setupMyPlayersTable()
        self.setupFrozenMyPlayers()


    def clearSearchBox(self):
        self.search_box.setText("")


    def coincidentScrollBars(self):
        # connects scroll bars 

        # active players and my_players (horizontal)
        self.my_players_table.horizontalScrollBar().valueChanged.connect(lambda: self.transferSignal1())

        # frozen players and my_players (vertical)
        self.my_players_table.verticalScrollBar().valueChanged.connect(lambda: self.transferSignal2())


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


    def quit(self):
        # terminates the PyQt
        design.QtWidgets.QApplication.quit()

        #terminates the program
        sys.exit()


    def setupActivePlayersTable(self):
        # adding columns
        self.num_active_players_table.setColumnCount(0)
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumn(self.num_active_players_table)

        # adding row
        self.num_active_players_table.setRowCount(1)

        current_gameweek = self.fpl_tool.current_gameweek
        for i in range (current_gameweek, 39):
            number_of_active = str(self.calculateActivePlayersColumn(i - current_gameweek + 1))
            item = design.QtWidgets.QTableWidgetItem(number_of_active)
            # text centered
            item.setTextAlignment(design.QtCore.Qt.AlignCenter)
            # not editable/clickable
            item.setFlags(design.QtCore.Qt.NoItemFlags)
            item.setForeground(design.QtGui.QBrush(design.QtGui.QColor(0, 0, 0)))
            # setup
            self.num_active_players_table.setItem(0, i - current_gameweek, item)


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


    def setupEvents(self):

        self.setupUi(self)

        self.setupIcons()

        self.setupStyle()

        # onclick functions for buttons
        self.setupOnclicks()

        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverButtons()

        self.setupMyPlayersTable()

        self.setupSearchBox()

        self.setupFixturesTable()

        self.setupFrozenFixtures()

        self.setupFrozenMyPlayers()

        self.setupActivePlayersTable()

        self.coincidentScrollBars()


    def setupFixturesTable(self):
        teams = self.fpl_tool.teams

        self.fixtures_table.setColumnCount(1)
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumn(self.fixtures_table, i)

        self.fixtures_table.setRowCount(0)
        for team in teams.getTeams():
            self.addRow(self.fixtures_table)

        table_row = 1
        for team in teams.getTeams():
            self.addTeamToTable(table_row, team)
            table_row += 1


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


    def addPlayerToFrozenFixtures(self, table_row, position):
        # returns number of a row
        number_of_players = 0
        for player in self.fpl_tool.players_array:
            if player.position == position:
                number_of_players += 1
                self.frozen_my_players.setVerticalHeaderItem(table_row, design.QtWidgets.QTableWidgetItem("G" + str(number_of_players))) # name of a row
                button = TableCell.TableCell() #creating button
                button.setText(player.getName()) # text
                button.changePlayerBackground(position, self.config) # colors
                button.setFontColor(self.config.font_color_string) # colors
                button.updateStyleSheet()
                button.clicked.connect(lambda: self.changePlayerActivity(self.config))
                self.frozen_my_players.setCellWidget(table_row, 0, button) # settling the button down
                table_row += 1
        return table_row


    def setupFrozenMyPlayers(self):
        players = self.fpl_tool.players_array

        table_row = 0
        self.frozen_my_players.setRowCount(0)

        # add rows
        for player in players:
            row_count = self.frozen_my_players.rowCount()
            self.frozen_my_players.setRowCount(row_count + 1)

        # adding goalkeepers
        table_row = self.addPlayerToFrozenFixtures(table_row, "Goalkeeper")

        # adding defenders
        table_row = self.addPlayerToFrozenFixtures(table_row, "Defender")

        # adding midfielders
        table_row = self.addPlayerToFrozenFixtures(table_row, "Midfielder")

        # adding forwards
        table_row = self.addPlayerToFrozenFixtures(table_row, "Forward")


    def setupHoverButtons(self):
        # main buttons
        list_of_buttons = [self.Planner, self.TeamDifficulty, self.Fixtures, self.Account, self.Quit, self.change_team_id_button, self.light_mode_button, self.dark_mode_button, self.custom_mode_button, self.add_player]

        for button in list_of_buttons:
            button.setStyleSheet("QPushButton::hover"
            "{"
                "background-color : "+ self.config.hover_menu_color +";"
            "}")
            button.setCursor(design.QtGui.QCursor(design.QtCore.Qt.PointingHandCursor))

        # other buttons
        self.cancel_button.setCursor(design.QtGui.QCursor(design.QtCore.Qt.PointingHandCursor))
        self.reset_button.setCursor(design.QtGui.QCursor(design.QtCore.Qt.PointingHandCursor))


    def setupIcons(self):
        # menu
        self.Planner.setIcon(design.QtGui.QIcon('icons/icon_planner.png'))
        self.TeamDifficulty.setIcon(design.QtGui.QIcon('icons/icon_team_difficulty.png'))
        self.Fixtures.setIcon(design.QtGui.QIcon('icons/icon_quit.png'))
        self.Account.setIcon(design.QtGui.QIcon('icons/icon_account.png'))
        self.Quit.setIcon(design.QtGui.QIcon('icons/icon_quit.png'))

        # cancel
        self.cancel_button.setIcon(design.QtGui.QIcon('icons/icon_cancel.png'))

        # reset
        self.reset_button.setIcon(design.QtGui.QIcon('icons/icon_reset.png'))


    def setupMyPlayersTable(self):
        self.my_players_table.setColumnCount(1)
        # adding columns
        for i in range (self.fpl_tool.current_gameweek, 39):
            self.addColumn(self.my_players_table, i)

        self.my_players_table.setRowCount(0)
        # adding rows for players
        for player in self.fpl_tool.players_array:
            self.addRow(self.my_players_table)

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
        self.custom_mode_button.clicked.connect(lambda: self.changeMode("custom"))

        # add player (planner table)
        self.add_player.clicked.connect(lambda: self.addConceptPlayer())
        self.cancel_button.clicked.connect(lambda: self.clearSearchBox())

        # reset
        self.reset_button.clicked.connect(lambda: self.changeAllToActive(self.config))

        # change team id
        self.change_team_id_button.clicked.connect(lambda: self.changeTeamId())


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


    def setupStyle(self):
        self.centralwidget.setStyleSheet(
        "QWidget#centralwidget {\n"
        "   background-color:" + self.config.main_background_color + ";\n"
        "}\n"
        "\n"
        "QWidget QPushButton{ \n"
        "   background-color: " + self.config.button_background_color + ";\n"
        "   border-radius:10px;\n"
        "}\n"
        "\n"
        "QWidget {\n"
        "   background-color: transparent;\n"
        "}\n"
        "\n"
        ""
        )
        self.my_players_table.setStyleSheet(
        "QTableWidget#my_players_table{\n"
        "   background-color:" + self.config.main_background_color + ";\n"
        "}\n"
        )
        self.frozen_my_players.setStyleSheet(
        "QTableWidget#frozen_my_players{\n"
        "   background-color:" + self.config.main_background_color + ";\n"
        "}\n"
        )
        self.cancel_button.setStyleSheet(
        "QPushButton#cancel_button{\n"
        "   background-color: transparent;\n"
        "}\n"
        )

        if self.config.mode == "custom":
            self.centralwidget.setStyleSheet(
            "QWidget#centralwidget {\n"
            "   background-image: url(\"C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png\");\n"
            "}\n"
            "\n"
            "QWidget QPushButton{ \n"
            "   background-color: " + self.config.button_background_color + ";\n"
            "   border-radius:10px;\n"
            "}\n"
            "\n"
            "QWidget {\n"
            "   background-color: transparent;\n"
            "}\n"
            "\n"
            ""
            )
        self.home_logo.setPixmap(design.QtGui.QPixmap(self.config.premier_league_logo_path))


    def showCurrentDifficulty(self, button, team_index):
        # updates text on a button
        difficulty = self.fpl_tool.teams.getTeamById(team_index).getDifficulty()
        if difficulty == 1:
            button.setText("very easy")
            button.setStyleSheet("background-color: " + self.config.difficulty1_color_string)
        if difficulty == 2:
            button.setText("easy")
            button.setStyleSheet("background-color: " + self.config.difficulty2_color_string)
        if difficulty == 3:
            button.setText("medium")
            button.setStyleSheet("background-color: " + self.config.difficulty3_color_string)
        if difficulty == 4:
            button.setText("hard")
            button.setStyleSheet("background-color: " + self.config.difficulty4_color_string)
        if difficulty == 5:
            button.setText("very hard")
            button.setStyleSheet("background-color: " + self.config.difficulty5_color_string)


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


    def transferSignal1(self):
        value = self.my_players_table.horizontalScrollBar().value()
        self.num_active_players_table.horizontalScrollBar().setValue(value)


    def transferSignal2(self):
        value = self.my_players_table.verticalScrollBar().value()
        self.frozen_my_players.verticalScrollBar().setValue(value)


    def updateBackgroundColors(self):
        # planner
        rows = self.my_players_table.rowCount()
        columns = self.my_players_table.columnCount()

        # check every cell
        for j in range (1, columns):
            for i in range (0, rows):
                self.my_players_table.cellWidget(i, j).changeBackground()

        # fixtures
        rows = self.fixtures_table.rowCount()
        columns = self.fixtures_table.columnCount()

        # check every cell
        for j in range (1, columns):
            for i in range (0, rows):
                self.fixtures_table.cellWidget(i, j).changeBackground()


    def updateEverything(self):
        self.showDifficulties()

        self.setupChangeTeamsDifficulty()

        self.setupHoverButtons()

        self.setupMyPlayersTable()

        self.setupFixturesTable()

        self.setupFrozenFixtures()

        self.setupFrozenMyPlayers()

        self.setupStyle()

        self.setupActivePlayersTable()


    def updateTable(self, table):
        # updates background and font colors of a table cells
        rows = table.rowCount()
        columns = table.columnCount()
        print(rows, columns)

        # check every cell
        for j in range (1, columns):
            for i in range (0, rows):
                table.cellWidget(i, j).changeBackground(self.config, self.fpl_tool)


    def updateTables(self):
        print("D")
        print("DDD", self.fpl_tool.teams.teams[0].difficulty)
        tables = [self.my_players_table, self.fixtures_table]
        for table in tables:
            self.updateTable(table)


# sorted to this point