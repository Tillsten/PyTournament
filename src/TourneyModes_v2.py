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
        self.rounds.append(Round(self.participants, self.freedraw))
        self.actual_round = self.rounds[-1]    
        self.games_open = self.actual_round.games_open
    
    def start_open_game(self, id = 0):
        starting_game = self.actual_round.games_open.pop(id)
        starting_game.status = Game.in_progress   
        self.actual_round.games_in_progress.append(starting_game)
        
    
    def show_games_open(self):
        print "Offene Spiele:"
        print "--------------------"
        
        for i in self.actual_round.games_open: print i
        print "\n"
        
    def show_games_finished(self):
        print "Fertige Spiele:"
        print "--------------------"
        for i in self.actual_round.games_finnished: print i
        print "\n"
    
    def show_games_inprogress(self):
        print "Laufende Spiele:"
        print "--------------------"
        
        for i in self.actual_round.games_in_progress: print i
        print "\n"    
    
    def insert_result(self, result, id = 0):
        fin_game = self.actual_round.games_in_progress.pop(id)
        fin_game.insert_result(result)
        self.actual_round.games_finnished.append(fin_game)
        if self.actual_round.games_open == [] and self.actual_round.games_in_progress == []:
            #print "--------- Round result ---------"
            #self.show_games_finished()
            self.next_round()
            #print "--------- Next Round -----------"
    
    def next_round(self):        
        left_players = [k.winner for k in self.actual_round.games_finnished]        
        if self.finnished:
            pass
        elif len(left_players) == 2:            
            self.finnished = True                    
            self.finals()
        else:
            print ("1/" + str(len(left_players)) + "-Finals")
            self.rounds.append(Round(left_players, self.freedraw))
            self.actual_round = self.rounds[-1]    
            self.games_open = self.actual_round.games_open
    
    def finals(self):
        assert(len(self.actual_round.games_finnished) == 2)
        #print "----Finals---"
        
        final = Round([k.winner for k in self.actual_round.games_finnished], self.freedraw)
        small_final = Round([k.loser for k in self.actual_round.games_finnished], self.freedraw)
        final.games_open.append(small_final.games_open[0])
        final.games.append(small_final.games_open[0])
        self.rounds.append(final)
        self.actual_round = final        
        #print self.actual_round.games
        
        
    def rankings(self):
        rank = []
        tmp_rounds = self.rounds[:]
        r = tmp_rounds.pop()
        print r.games[0]
        ## First four places needs special treatment. 
        rank.append(r.games[0].winner)
        rank.append(r.games[0].loser)
        
        rank.append(r.games[1].winner)
        rank.append(r.games[1].loser)
        
        r = tmp_rounds.pop()
        while tmp_rounds != []:
            r = tmp_rounds.pop()
            rank.extend([game.loser for game in r.games if game.loser != self.freedraw])
            
        for i in range(len(rank)): print str(i + 1) + "   " + str(rank[i])
            

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
    sko.start_open_game()
    sko.insert_result([(3, 8)], 0)
    sko.start_open_game()    
    sko.insert_result([(8, 3)], 0)    
    sko.start_open_game()
    sko.start_open_game()   
    sko.insert_result([(3, 4), (5, 9)])
    sko.insert_result([(3, 4), (5, 9)])
    sko.start_open_game()
    sko.start_open_game() 
    sko.insert_result([(3, 4), (5, 9)])
    sko.insert_result([(3, 4), (5, 9)])
#    print "rounds"
#    for i in sko.rounds:        
#            for j in (i.games):
#                print j
    sko.rankings()

    
    
    
