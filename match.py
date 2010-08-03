#!/usr/bin/env python
'''Class Match:
Represents a given match of a certain game. Match is a dumb class, completely submissive to Game, and only knows Table, Teams and Dealer. Match holds the current game state.
'''

import table
import dealer
import teams

__author__ = "Esteban Martinez and Rodney Phillips"
__copyright__ = "Copyright 2010"
__credits__ = ["Esteban Martinez", "Rodney Phillips"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Esteban Martinez and Rodney Phillips"
__email__ = "esteban.a.martinez at gmail dot com, rodneyph at gmail dot com"
__status__ = "Production"

class Match:
    def __init__(self):
        self.dealer = Dealer()
        self.table = Table()
        self.teams = Teams()
        self.turn = 0

    def get_alias(self, email):
        return self.dealer.get_alias(player)

    def get_score(self, team):
        return self.team.get_score()

    def add_player(self,player):
        pass

    def get_players(self):
	for team in self.teams:
		ret += team.get_players()
	return ret

    def increase_score(self,team,n):
	self.team.add_points(n)

    def get_host_email(self):
        for team in self.teams:
            for player in team:
                if player.is_host: return player.email

    def get_current_player_email(self):
        return self.teams[self.turn//len(self.teams)].player[self.turn%len(self.teams)].email

    def get_total_players(self):
        ret = 0
        for team in self.teams:
            ret+=self.team.player_amount
        return ret
    
    def next_player(self):
        self.turn = (self.turn+1)%self.get_total_players

    def is_turn_of(self,email):
        return self.get_current_player_email() = email
    
    def is_bet_pending(self,bet_type):
        pass

