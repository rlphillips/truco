#!/usr/bin/env python
'''Class Rulebook:
Belongs to Game, holds all the rules in the game. Will be checked in case of everything (for example, to check whether a player can play a card or not).
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

class Rulebook:
    def __init__(self):
        self.hier = {'4*':0,'5*':1,'6*':2,'7b':3,'7c':3,'10*':4,'11*':5,'12*':6,
                '1o':7,'1c':7,'2*':8,'3*':9,'7o':10,'7e':11,'1b':12,'1e':13}
        self.envidovalue = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,10:0,11:0,12:0}
    def can_play_card(self):
        pass

    def get_hier(self,card):
        key = str(card['number'])+card['suit'][0]
        if (str(card['number'])+'*') in self.hier:
            return self.hier[str(card['number'])+'*']
        elif key in self.hier:
            return self.hier[key]
        else: return -1

    def get_bet_type(self):
        pass

    #devuelve 0 si son iguales
    def get_higher_card(self,card1,card2):
        if(self.get_hier(card1)>self.get_hier(card2)):
            return card1
        elif self.get_hier(card1)<self.get_hier(card2)):
            return card2
        else:
            return 0
    
    def get_envido_hand(self, hand):
        return

    def get_envido_card(self,card):
        if card['number'] in self.envidovalue:
            return self.envidovalue[card['number']]
        else:
            return -1
    
    def has_envido(self,hand):
        suits = [ card['suit'] for card in hand]
        for suit in suits:
            if suits.count(suit)>=2:
                return true
    

    def get_highest_envido(hand):
        pass
