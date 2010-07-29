#!/usr/bin/env python
'''Class Translator:
Translates between emesene events and game events. Outputs received messages string (a stripped version) to the parser in class Game, eventually receives a string from Game to print as a message.
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

class Translator:
    def __init__(self):
        pass

    def convert_to_standard_form(self, message):
        message = message.lower()
        message = message.strip()
        message = message.translate(maketrans('αινσϊ','aeiou'))
        return message;

    def from_messenger_to_game(self, event):
        '''Translates an emesene event to a game event. TODO: This is almost pseudocode yet.'''
        if event.type == 'message':
            command_list = self.parse_message(event.text)
            origin_player = event.player
            for command_name in command_list.keys():
                command = {'name': command_name, 'arguments': command_list[command_name], 'player': origin_player}
                current_game.push_command(command)
            
    def from_game_to_messenger(self, event):
        '''Translates a game event to an emesene event. TODO: This is almost pseudocode yet.'''
        message = convert_event_to_message(event)
        emesene.write(message)
