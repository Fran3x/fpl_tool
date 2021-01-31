
import urllib.request, json 


class Tool:


    #translates team_id to team abbreviation
    team_abb = {
        1 : "ars",
        2 : "avl",
        3 : "bri",
        4 : "bur",
        5 : "che",
        6 : "cry",
        7 : "eve",
        8 : "ful",
        9 : "lee",
        10 : "lei",
        11 : "liv",
        12 : "mci",
        13 : "mun",
        14 : "new",
        15 : "she",
        16 : "sou",
        17 : "tot",
        18 : "wba",
        19 : "whu",
        20 : "wol"
    }


    team_difficulty = [3 for x in range (20)]


    def saveTeamDifficulties(self):
        file = open("team_difficulties.txt", "w")
        for team_dif in self.team_difficulty:
            file.write(str(team_dif))

    def readTeamDifficulties(self):
        file = open("team_difficulties.txt", "r")
        content = file.read()
        for i in range (20):
            self.team_difficulty[i - 1] = int(content[i - 1])
        print(self.team_difficulty)


    #translates team_id to team abbreviation
    team_abb = {
        1 : "ars",
        2 : "avl",
        3 : "bri",
        4 : "bur",
        5 : "che",
        6 : "cry",
        7 : "eve",
        8 : "ful",
        9 : "lee",
        10 : "lei",
        11 : "liv",
        12 : "mci",
        13 : "mun",
        14 : "new",
        15 : "she",
        16 : "sou",
        17 : "tot",
        18 : "wba",
        19 : "whu",
        20 : "wol"
    }


with urllib.request.urlopen("https://fantasy.premierleague.com/api/bootstrap-static/") as url:
    data = json.loads(url.read())
    #print(team_abb[data['elements'][3]["team"]])
    #print(str(data['elements'][3]))

# for i in range (77):
#     if (data['elements'][i]['team'] == 1):
#         print(str(data['elements'][i]['web_name']))

