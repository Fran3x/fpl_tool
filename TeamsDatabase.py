
import urllib.request, json
import Team


class TeamsDatabase:
    def __init__(self):
        self.teams = [ ]
        # array structure - [team_id][gameweek][list of fixtures presented as [opponent_id, H/A]]
        self.fixtures_array = [[[] for y in range(38)] for z in range(20)]
        self.getFixtures()
        self.updateDatabase()

    def updateDatabase(self):
        self.teams.append(Team.Team(1, "Arsenal", "ars", self.fixtures_array[0]))
        self.teams.append(Team.Team(2, "Aston Villa", "avl", self.fixtures_array[1]))
        self.teams.append(Team.Team(3, "Brighton", "bri", self.fixtures_array[2]))
        self.teams.append(Team.Team(4, "Burnley", "bur", self.fixtures_array[3]))
        self.teams.append(Team.Team(5, "Chelsea", "che", self.fixtures_array[4]))
        self.teams.append(Team.Team(6, "Crystal Palace", "cry", self.fixtures_array[5]))
        self.teams.append(Team.Team(7, "Everton", "eve", self.fixtures_array[6]))
        self.teams.append(Team.Team(8, "Fulham", "ful", self.fixtures_array[7]))
        self.teams.append(Team.Team(10, "Leeds", "lee", self.fixtures_array[9]))
        self.teams.append(Team.Team(9, "Leicester", "lei", self.fixtures_array[8]))
        self.teams.append(Team.Team(11, "Liverpool", "liv", self.fixtures_array[10]))
        self.teams.append(Team.Team(12, "Manchester City", "mci", self.fixtures_array[11]))
        self.teams.append(Team.Team(13, "Manchester United", "mun", self.fixtures_array[12]))
        self.teams.append(Team.Team(14, "Newcastle", "new", self.fixtures_array[13]))
        self.teams.append(Team.Team(15, "Sheffield United", "she", self.fixtures_array[14]))
        self.teams.append(Team.Team(16, "Southampton", "sou", self.fixtures_array[15]))
        self.teams.append(Team.Team(17, "Tottenham", "tot",self.fixtures_array[16]))
        self.teams.append(Team.Team(18, "West Bromwich Albion", "wba", self.fixtures_array[17]))
        self.teams.append(Team.Team(19, "West Ham United", "whu", self.fixtures_array[18]))
        self.teams.append(Team.Team(20, "Wolverhampton", "wol", self.fixtures_array[19]))


    def getFixtures(self):
        with urllib.request.urlopen("https://fantasy.premierleague.com/api/fixtures/") as url_fixtures:
            fixtures = json.loads(url_fixtures.read())
        for fixture in fixtures:
            team_h = int(fixture["team_h"])
            team_a = int(fixture["team_a"])
            if fixture["event"]:
                gameweek = int(fixture["event"])
                team_h_fixture = [team_a, "H"]
                team_a_fixture = [team_h, "A"]
                self.fixtures_array[team_h - 1][gameweek - 1].append(team_h_fixture)
                self.fixtures_array[team_a - 1][gameweek - 1].append(team_a_fixture)


    def getTeamByName(self, name):
        for team in self.teams:
            if team.name == name:
                return team


    def getTeamById(self, new_id):
        for team in self.teams:
            if team.id == new_id:
                return team


    def saveTeamDifficulties(self):
        file = open("team_difficulties.txt", "w")
        for team in self.teams:
            file.write(str(team.getDifficulty()))


    def readTeamDifficulties(self):
        file = open("team_difficulties.txt", "r")
        content = file.read()
        for i in range (1, 21):
            # sets difficulty of given team
            self.getTeamById(i).setDifficulty(int(content[i - 1]))

    def getTeams(self):
        return self.teams
