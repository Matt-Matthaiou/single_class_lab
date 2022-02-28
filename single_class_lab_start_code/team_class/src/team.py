class Team:

    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach
        self.points = 0 

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, name):
        if name in self.players:
            return True
        else:
            return False 
    
    def play_game(self, result):
        if result == True:
            self.points += 3