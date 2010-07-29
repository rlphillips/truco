#!/usr/bin/env python
'''Class Card:
Belongs to Hand. Holds the number and suit of the card.
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

class Card:
    def __init__(self, number, suit):
	self.number = number
        self.suit = suit
