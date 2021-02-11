
class Player:
    # attributes:
    # id
    # name
    # team_id
    # position: G D M F
    # 

    def __init__(self, new_id, new_name, new_team_id, new_position, new_first_name, new_last_name):
        self.id = new_id
        self.name = new_name
        self.team_id = new_team_id
        self.position = new_position
        self.first_name = new_first_name
        self.last_name = new_last_name

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def createCompleterString(self, team_abbrevation):
        self.completer_string = self.first_name + " " + self.last_name + "(" + team_abbrevation.upper() + ")"
        return self.completer_string

    def getTeamId(self):
        return self.team_id