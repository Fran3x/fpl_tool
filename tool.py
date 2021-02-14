
import urllib.request, json 
import pprint

from datetime import datetime

import PlayersDatabase
import TeamsDatabase


class Tool:
    def __init__(self):

        self.teams = TeamsDatabase.TeamsDatabase()

        self.players = PlayersDatabase.PlayersDatabase()

        self.picks_array = [ ] # keeps ids of picked players
        self.players_array = [ ] # keeps names of picked players

        self.getData()


    def getData(self):
        # calls all the functions used to get specific parts of data
        self.loadData() # loads data from fpl api json file

        self.teams.readTeamDifficulties() # reads from team_difficulties file

        self.next_gameweek = self.getNextGameweek()
        self.current_gameweek = self.next_gameweek - 1

        self.getPlayersIds()
        self.getPlayersNames()



    def loadData(self):
        with urllib.request.urlopen("https://fantasy.premierleague.com/api/bootstrap-static/") as url:
            self.data = json.loads(url.read())


    def getPlayersIds(self):
        # https://fantasy.premierleague.com/api/entry/8487/event/21/picks/
        # gets my players for current gameweek
        if self.current_gameweek > 0:
            with urllib.request.urlopen("https://fantasy.premierleague.com/api/entry/8487/event/"+ str(self.current_gameweek) +"/picks/") as url_picks:
                picks = json.loads(url_picks.read())['picks']
                for pick in picks:
                    #print("P", pick)
                    self.picks_array.append(pick['element'])
                #print(self.picks_array)


    def getPlayersNames(self):
        # gets name of my picked players
        for pick_id in self.picks_array:
            self.players_array.append(self.players.getPlayerById(pick_id))





    #print(team_abb[data['elements'][3]["team"]])
    #print(str(data['elements'][3]))

    # for i in range (77):
    #     if (data['elements'][i]['team'] == 1):
    #         print(str(data['elements'][i]['web_name']))



    def getNextGameweek(self):
        next_gameweek = 1

        # getting number of a next gameweek
        for i in range (1, 38):
            now = datetime.now()
            date = self.data['events'][i - 1]['deadline_time']
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
            hour = int(date[11:13])
            minute = int(date[14:16])
            second = int(date[17:19])

            if now > datetime(year, month, day, hour, minute ,second):
                next_gameweek += 1

        return next_gameweek



