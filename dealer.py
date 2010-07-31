#!/usr/bin/env python
'''Class Dealer:
Belongs to Match, deals the cards and keeps the score.
'''

import random
import player

__author__ = "Esteban Martinez and Rodney Phillips"
__copyright__ = "Copyright 2010"
__credits__ = ["Esteban Martinez", "Rodney Phillips"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Esteban Martinez and Rodney Phillips"
__email__ = "esteban.a.martinez at gmail dot com, rodneyph at gmail dot com"
__status__ = "Production"

class Dealer:
    def __init__(self):
        self.players_roster = {}
        self.score_sheet = {}
        suits = ['oro', 'copa', 'basto', 'espada']
        numbers = range(1, 7) + range(10, 12)
        #self.deck = [{'number': number, 'suit': suit} for number in numbers for suit in suits]
	
	#El dealer no debería conocer a los jugadores.
    #def get_alias(self, player):
    #    pass
	#El dealer no va a almacenar el puntaje, va a quedar en team
    #def get_score(self, team):
    #    return self.score_sheet[team]
	#El dealer no va a conocer a los jugadores.
    #def add_player(self, player):
    #    pass

    def give_cards(self, hand_size):
        cards = random.sample(self.deck, hand_size)
        for card in cards:
        	self.deck.remove(card)
	return cards

    def shuffle(self):
	self.deck = original_deck

    def assign_deck(self,deck):
	self.original_deck = deck
            
