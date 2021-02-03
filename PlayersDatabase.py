
from Player import Player
import urllib.request, json

class PlayersDatabase:
    def __init__(self):
        self.players = [ ]
        self.updateDatabase()

    def loadData(self):
        with urllib.request.urlopen("https://fantasy.premierleague.com/api/bootstrap-static/") as url:
            self.data = json.loads(url.read())

    def updateDatabase(self):
        self.loadData()

        for player in self.data["elements"]:
            new_id = player["id"]
            new_name = player ["web_name"]
            new_team_id = player["team"]
            new_position_number = player["element_type"]
            if new_position_number == 1:
                new_position = "Goalkeeper"
            if new_position_number == 2:
                new_position = "Defender"
            if new_position_number == 3:
                new_position = "Midfielder"
            if new_position_number == 4:
                new_position = "Forward"

            self.players.append(Player(new_id, new_name, new_team_id, new_position))


    def getPlayerByName(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def getPlayerById(self, new_id):
        for player in self.players:
            if player.id == new_id:
                return player

    def getPlayersNames(self):
        output = []
        for player in self.players:
            output.append(player.getName())
        return output

