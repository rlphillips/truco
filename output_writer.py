#!/usr/bin/env python
'''Class OutputWriter:
Produces output strings to be sent to Translator, belongs to Game.
'''

import re
import string

__author__ = "Esteban Martinez and Rodney Phillips"
__copyright__ = "Copyright 2010"
__credits__ = ["Esteban Martinez", "Rodney Phillips"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Esteban Martinez and Rodney Phillips"
__email__ = "esteban.a.martinez at gmail dot com, rodneyph at gmail dot com"
__status__ = "Production"

class OutputWriter(CardGameOutputWriter):
    def __init__(self):
        pass

    def card_to_string(self, card):
        '''Returns the complete name of the card.'''
        card_suit = card.suit
        card_number = card.number
        card_name = self.number_to_string(card_number) + ' de ' + card_suit
        return card_name

    def convert_event_to_message(self, event):
        event_type = event['description']

        if event_type = 'print score':
            score_table = event['score_table']
            self.print_score(score_table)
        
        elif event_type = 'play card':
            card = event['card']
            player = event['player']
            message = player + ' tiró un ' + self.card_to_string(card) '.'      
            
        return message

    def format(self, message, format_type):    
        if format_type == 'public':
            border_size = 20
            border_character = '~'
        elif format_type == 'private':
            border_size = 5
            border_character = '#'
        formatted_message =  order_character * border_size + '\n' + message + '\n' + border_character * border_size
        return formatted_message

    def number_to_string(self, number):
        numbers_dict = {1: 'ancho', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete',\
                            8: 'ocho', 9: 'nueve', 10: 'sota', 11: 'caballo', 12: 'rey'}
        string = numbers_dict[number]
        return string

    def print_score(self, score_table):
        pass
        
