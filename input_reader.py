#!/usr/bin/env python
'''Class InputReader:
Parses input strings from Translator, belongs to Game.
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

class TrucoInputReader(CardGameInputReader):
    def __init__(self):
        pass
    
    def parse_bet(self, message):
        bet_names = ['quiero retruco', 'quiero vale cuatro', 'no quiero', 'quiero', 'contraflor al resto', \
                         'contraflor', 'flor', 'real envido', 'falta envido', 'envido', 'truco'}
        bet_places = {}
        bets = []

        for bet_name in bet_names:
            place = message.find(bet_name)
            bet_places[bet_name] = place

        for bet_name in bet_names:
            occurrences = message.count(bet_name)
            if occurrences >= 1:
                message = message.replace(bet_name, '')
                bet_list.push(bet_name)

        bets = sorted(bets, key = lambda bet_name: bet_places[bet_name])
        result = Command('bet', bets)
        return result

    def parse_explicit_command(self, message):
        tokens = message.split(' ,!')
        command_names = {'a': 'accept', 'accept': 'accept', 'b': 'bet', 'bet': 'bet', 't': 'play', 'tirar': 'play', 'p': 'play', 'play': 'play', 'q': 'accept', \
                             'quiero': 'accept', 'd': 'decline', 'decline': 'decline', 'noquiero': 'decline'}
        command_name = command_names[tokens.pop(0)]
        command_argument = command_names[tokens.pop(0)] #TODO: Warning! Check for bounds.
        
        if command_name == 'accept' or command_name == 'decline':
            result = Command('bets', [command_name])
        elif command_name == 'bet':
            result = Command('bets', [command_argument])
        elif command_name == 'play':
            result = Command('play', [command_argument])
        else:
            result = Command('', [])
        
        return result

    def parse_implicit_command(self, message):
        tokens = message.split('*')
        command_names = {'mira su mano': 'show hand', 'muestra su mano': 'display hand', 'se va al mazo': 'forfeit'}
        command_name = command_names[tokens.pop(0)]
        result = Command(command_name)
        return result

    def parse_message(self, message):
        '''Outputs all the read commands.'''
	if message.find('!') == 0: #Explicit commands.
            commands = self.parse_explicit_command(message)	
	elif message.find('*') == 0: #Natural commands.
            commands = self.parse_implicit_command(message)
        else: #Possible bets.
            commands = self.parse_bet(message)
	return commands

    def string_to_card(self, string):
        card = Card(0, '')
        tokens = string.split()
        if tokens.len() == 2: #Played card: 'caballo oro'
            card_number = self.string_to_number(tokens[0])
            card_suit = self.string_to_suit(tokens[1])
        elif (tokens.len() == 3 && tokens[1] == 'de'): #Played card: 'caballo de oro'
            card_number = self.string_to_number(tokens[0])
            card_suit = self.string_to_suit(tokens[2])
        return card

    def string_to_number(self, string):
        numbers = {'ancho': 1, 'ancho falso': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7,\
                            'ocho': 8, 'nueve': 9, 'diez': 10, 'sota': 10, 'once': 11, 'caballo': 11, 'doce': 12, 'rey': 12}
        number = numbers.get(string, 0)
        return number

    def string_to_suit(self, string):
        suits = {'oro': 'oro', 'oros': 'oro', 'copa': 'copa', 'copas': 'copa', 'basto': 'basto', 'bastos': 'basto',\
                          'espada': 'espada', 'espadas': 'espada'}
        suit = suits.get(string, '')
        return suit

    def read_input(self, message):
        self.parse_message(message)
        return 0
