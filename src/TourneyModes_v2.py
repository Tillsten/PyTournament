'''
Created on 26.01.2010

@author: Tillsten
'''
from TeamsAndPlayers import *
import random

class Round(object):
    def __init__(self, left_teams, freedraw):        
        self.games_open = []
        self.games_finnished = []
        self.games_in_progress = []          
        self.games = []
        while left_teams != []:
            a = left_teams.pop(0)
            b = left_teams.pop()
            g = Game(a, b)
            self.games.append(g)
            if b != freedraw:
                self.games_open.append(g)
                
            else:
                g.insert_result([(7, 3)])
                self.games_finnished.append(g)
        #print self.games
                
class Single_ko(object):    
    
    def __init__(self, players_per_team = 1):
        self.participants = []
        self.players_per_team = players_per_team
        self.rounds = []
        self.games_open = []
        self.games_finnished = []
        self.games_in_progress = []
        self.finnished = False
    
    def add_team(self, player):
        if self.players_per_team == 1:            
            self.participants.append(Single_team(player))
        if self.players_per_team == 2:
            self.participants.append(Double_team(player[0], player[1]))
    
    def start(self):
        self.freedraw = Single_team(Player("Freilos", "", 0))
        n = 1
        random.shuffle(self.participants)
        while len(self.participants) > 2 ** n:
            n += 1
        for i in range(len(self.participants), 2 ** n):
            self.participants.append(self.freedraw)        
        self.build_gametree(n)
        
        
    def build_gametree(self, n):
        self.games = []       
        left_teams = self.participants
        first_round = []
        while left_teams != []:
            a = left_teams.pop(0)
            b = left_teams.pop()
            g = Game(a, b)
            self.games.append(g)
            first_round.append(g)
            
            if b != self.freedraw:
                self.games_open.append(g)            
            else:
                g.insert_result([(7, 3)])
                self.games_finnished.append(g)
        while len(last_round) < 4:
            left_teams = [g.winner for g in last_round]
            while left_teams != []:
                a = left_teams.pop(0)
                b = left_teams.pop()
                g = Game(a, b)
                self.games.append(g)
                
        for i in self.games: print i
    

if __name__ == '__main__':
    import psyco
    psyco.full()
    anton = Single_team(Player("Anton", "A.", 1))
    bart = Single_team(Player("Bart", "B.", 2))
    caro = Single_team(Player("Caro", "C.", 3))
    dieter = Single_team(Player("Dieter", "D.", 4))
    edwin = Single_team(Player("Edwin", "E.", 5))
    fi = Single_team(Player("Fieter", "F.", 6))
    sko = Single_ko()
    sko.add_team(anton)
    sko.add_team(bart)
    sko.add_team(caro)
    sko.add_team(dieter)
    sko.add_team(edwin)
    sko.add_team(fi)
    sko.start()
#    sko.start_open_game()
#    sko.insert_result([(3, 8)], 0)
#    sko.start_open_game()    
#    sko.insert_result([(8, 3)], 0)    
#    sko.start_open_game()
#    sko.start_open_game()   
#    sko.insert_result([(3, 4), (5, 9)])
#    sko.insert_result([(3, 4), (5, 9)])
#    sko.start_open_game()
#    sko.start_open_game() 
#    sko.insert_result([(3, 4), (5, 9)])
#    sko.insert_result([(3, 4), (5, 9)])
#    print "rounds"
#    for i in sko.rounds:        
#            for j in (i.games):
#                print j
#    sko.rankings()

    
    
    
