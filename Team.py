
class Team:
    def __init__(self, team_id, team_name, team_abbrevation, team_fixtures):
        self.id = team_id
        self.name = team_name
        self.abb = team_abbrevation
        self.fixtures = team_fixtures
        self.difficulty = 3

    def setDifficulty(self, new_difficulty):
        self.difficulty = new_difficulty

    def getDifficulty(self):
        return self.difficulty

    def getName(self):
        return self.name

    def getAbb(self):
        return self.abb

    def getOpponentsOfTeam(self):
        return self.fixtures