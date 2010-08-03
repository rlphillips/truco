#!/usr/bin/env python
'''Class Team:
Represents a given team, holds a bunch of players.
'''

import string

__author__ = "Esteban Martinez and Rodney Phillips"
__copyright__ = "Copyright 2010"
__credits__ = ["Esteban Martinez", "Rodney Phillips"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Esteban Martinez and Rodney Phillips"
__email__ = "esteban.a.martinez at gmail dot com, rodneyph at gmail dot com"
__status__ = "Production"

class Team:
    def __init__(self):
        self.players = []
	self.score = 0
	self.name = ""
    
    def get_players:
	return self.players

    def change_score(self, n)
	self.score += n

    def get_score(self):
	return self.score

    def set_name(self,name):
	self.name = name

    def has_player(self,player):
	return player in self.player

    def player_amount(self):
        return len(self.players)
