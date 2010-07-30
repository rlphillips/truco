#!/usr/bin/env python
'''Class Table:
Belongs to match, holds the played cards and bets.
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

class Table:
    def __init__(self):
        self.cards = []
        self.bets = {}
        self.round_number = 1
        self.turn = 1
    
    def add_card(self, card):
        self.cards[self.round_number]
    
    def add_bet(self, bet_type, bet):
        self.bets[bet_type] = bet
