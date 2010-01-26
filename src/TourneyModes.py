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
        self.games_open = []
        while left_teams != []:
            a = left_teams.pop(0)
            b = left_teams.pop()
            if b != freedraw:
                self.games_open.append(Game(a, b))
            else: 
                freedr = Game(a, b)
                freedr.insert_result([(7, 3)])
                self.games_finnished.append(freedr)
                
class Single_ko(object):    
    def __init__(self, players_per_team = 1):
        self.participants = []
        self.players_per_team = players_per_team
        self.rounds = []
        self.games_open = []
    
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
        self.rounds.append(Round(self.participants, self.freedraw))
        self.actual_round = self.rounds[-1]    
        self.games_open = self.actual_round.games_open
    
    def start_open_game(self, id = 0):
        starting_game = self.actual_round.games_open.pop(id)
        starting_game.status = Game.in_progress   
        self.actual_round.games_in_progress.append(starting_game)
        
    
    def show_games_open(self):
        for i in self.actual_round.games_open: print i
    def show_games_finished(self):
        for i in self.actual_round.games_finnished: print i
    def show_games_inprogress(self):
        for i in self.rounds[-1].games_in_progress: print i    
    
    def insert_result(self, result, id = 0):
        fin_game = self.rounds[-1].games_in_progress.pop(id)
        fin_game.insert_result(result)
        self.rounds[-1].games_finnished.append(fin_game)
        if self.actual_round.games_open == [] and self.actual_round.games_in_progress == []:
            self.next_round()
    
    def next_round(self):
        left_players = [k.winner for k in self.actual_round.games_finnished]
        self.rounds.append(Round(left_players, self.freedraw))
        self.actual_round = self.rounds[-1]    
        self.games_open = self.actual_round.games_open
        
        
        
        
        
            
if __name__ == '__main__':
    anton = Single_team(Player("Anton", "A.", 1))
    bart = Single_team(Player("Bart", "B.", 2))
    caro = Single_team(Player("Caro", "C.", 3))
    dieter = Single_team(Player("Dieter", "D.", 3))
    sko = Single_ko()
    sko.add_team(anton)
    sko.add_team(bart)
    sko.add_team(caro)
    #sko.add_team(dieter)
    sko.start()
    sko.start_open_game()
    sko.show_games_inprogress()
    sko.show_games_open()
    sko.show_games_finished()
    sko.insert_result([(3, 8)], 0)
    for i in sko.games_open: print i
