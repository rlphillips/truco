import string
import re

class Translator:
    '''Translates between emesene events and game events.'''
    def __init__(self):
        self.asdf = "asdf"

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

    def convert_to_standard_form(self, message):
        message = message.lower()
        message = message.strip()
        message = message.translate(maketrans('áéíóú','aeiou'))
        return message;

    def parse_message(self, message):
        '''Outputs a dictionary, whose keys are the commands included in message, and whose entries are the command arguments.'''
        command_list = {}

	#Explicit commands.
	if message.find('!') == 0:
            tokens = message.split(' ,!')
            command_names = {'a': 'accept', 'b': 'bet', 't': 'play', 'p': 'play', 'q': 'accept', 'd': 'decline'}
            command_name = command_names[tokens.pop(0)]
            command_arguments = tokens
            command_list[command_name] = command_arguments
            
	#Natural commands.
	if message.find('*') == 0:
            tokens = message.split('*')
            command_names = {'mira su mano': 'show hand', 'muestra su mano': 'display hand', 'se va al mazo': 'forfeit'}
            command_name = actions[tokens.first()]
            command_list[command_name] = []

        #Bets.
        bet_names = ['quiero retruco', 'quiero vale cuatro', 'no quiero', 'quiero', 'contraflor al resto', \
                         'contraflor', 'flor', 'real envido', 'falta envido', 'envido', 'truco'}
        bet_places = {}
        bet_list = []

        for bet_name in bet_names:
            place = message.find(bet_name)
            bet_places[bet_name] = place

        for bet_name in bet_names:
            occurrences = message.count(bet_name)
            if occurrences >= 1:
                message = message.replace(bet_name, '')
                bet_list.push(bet_name)

        bet_list = sorted(bet_list, key = lambda bet_name: bet_places[bet_name])
        command_list['bet'] = bet_list

	return command_list

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
        '''TODO'''
        asdf = 'asdf'

    def string_to_card(self, string):
        card = Card(0, '')
        tokens = string.split()
        if tokens.len() == 2:
            card_number = self.string_to_number(tokens[0])
            card_suit = self.string_to_suit(tokens[1])
        elif (tokens.len() == 3 && tokens[1] == 'de'):
            card_number = self.string_to_number(tokens[0])
            card_suit = self.string_to_suit(tokens[2])
        return card

    def string_to_number(self, string):
        numbers_dict = {'ancho': 1, 'ancho falso': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7,\
                            'ocho': 8, 'nueve': 9, 'diez': 10, 'sota': 10, 'once': 11, 'caballo': 11, 'doce': 12, 'rey': 12}
        output_number = numbers_dict.get(string, 0)
        return output_number

    def string_to_suit(self, string):
        suits_dict = {'oro': 'oro', 'oros': 'oro', 'copa': 'copa', 'copas': 'copa', 'basto': 'basto', 'bastos': 'basto',\
                          'espada': 'espada', 'espadas': 'espada'}
        suit = suits_dict.get(string, '')
        return suit

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
