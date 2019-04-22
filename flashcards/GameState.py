from .State import State
from .status_messages import *
import random as rand
import sys


class GameState(State):
    def __init__(self, new_flashcards):
        self.flashcards = new_flashcards

    def print_help(self):
        print('Available commands:')
        print('<< - go back to menu')
        print('!! - quit')
        print('?? - display this message\n')

    def display(self):
        print('Welcome! The vocab game will now start.')
        self.print_help()

        groups = self.flashcards.active_groups

        word_list = []
        for key, value in groups.items():
            word_list.extend(list(value.get_vocab_list().items()))

        # word_list.extend(list((value.get_vocab_list().items() for key, value in groups.items) for key, value in groups.items()))
        while True:
            word = rand.choice(word_list)

            user_input = input(word[0] + ': ')
            if user_input == word[1]:
                print_success('Correct!')
            elif user_input == '<<':
                self.flashcards.state = self.flashcards.menu_state
            elif user_input == '??':
                self.print_help()
            elif user_input == '!!':
                print('Bye, bitch.')
                sys.exit(0)
            else:
                print_fail('So close! The correct word was ' + word[1])
