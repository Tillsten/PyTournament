'''
Created on 26.01.2010

@author: Till Stensitzki
'''
class Player(object):            
    def __init__(self, name, first_name, player_id):
        self.name = name
        self.first_name = first_name
        self.player_id = player_id
    def __str__(self):
        return self.first_name + " " + self.name + "  " + str(self.player_id)

class Single_team(object):
    def __init__(self, player1):
        self.player1 = player1
        self.played_teams = []
    def __str__(self):
        return str(self.player1)
    
class Double_team(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.played_teams = []
        
class Participants(list):
    def __init__(self):
        list.__init()



class Game(object):
    
    # Gamestatus enum
    (is_open, in_progress, is_finnished) = ("is open", "in progress", "is finnished")
    
    def __init__(self, team1, team2, sets = 1):
        self.status = Game.is_open
        self.result = None
        self.team1 = team1
        self.team2 = team2
        
    def insert_result(self, result):
        '''Method to insert the result of a game. 
        Result is a list of tuples, one for each set.
        '''
        self.result = result
        self.status = Game.is_finnished
        won_sets = 0
        
        for (i, j) in result:            
            if i > j:               
                won_sets += 1                
            if i < j: 
                won_sets -= 1                 
        if won_sets == 0:
            self.winner = None
        else: 
            if won_sets > 0: 
                self.winner = self.team1
                self.loser = self.team2
            else: 
                self.loser = self.team1
                self.winner = self.team2
    
    def __str__(self):
        r = "".join(["", str(self.team1), "  vs  ", str(self.team2)])        
        if self.result != None:
            r += "   ".join([str(i) for i in self.result]) 
            r += "".join(["   Winner: ", str(self.winner)])            
        return r             
        
            
        
if __name__ == '__main__':
    anton = Single_team(Player("Anton", "A.", 1))
    bart = Single_team(Player("Bart", "B.", 2))
    caro = Single_team(Player("Caro", "C.", 3))
    dieter = Single_team(Player("Dieter", "D.", 3))
    g1 = Game(anton, bart)
    g2 = Game(caro, dieter)
    print g1
    g1.insert_result([(6, 4), (3, 6), (6, 1)])
    print g1
    g2.insert_result([(6, 4), (4, 6)])
    print g2

