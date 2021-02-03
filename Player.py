
class Player:
    # attributes:
    # id
    # name
    # team_id
    # position: G D M F
    # 

    def __init__(self, new_id, new_name, new_team_id, new_position):
        self.id = new_id
        self.name = new_name
        self.team_id = new_team_id
        self.position = new_position

    def getName(self):
        return self.name