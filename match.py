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

    def get_alias(self, email):
        return self.dealer.get_alias(player)

    def get_score(self, team):
        return self.dealer.get_score(team)

    def add_player(self, player):
        pass
