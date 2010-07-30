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
        self.deck = [{'number': number, 'suit': suit} for number in numbers for suit in suits]

    def get_alias(self, player):
        pass

    def get_score(self, team):
        return self.score_sheet[team]

    def add_player(self, player):
        pass

    def deal_hands(self, hand_size):
        for player in self.player_roster.keys():
            cards = random.sample(self.deck, hand_size)
            for card in cards:
                self.deck.remove(card)
            player.add_cards(cards)
            
