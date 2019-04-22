from .State import State
from .status_messages import *
import sys


class MenuState(State):
    def __init__(self, new_flashcards):
        self.flashcards = new_flashcards

    @classmethod
    def dict_keys_to_list(self, dictionary):
        # keys = []
        # for k in dictionary.keys():
        #     keys.append(k)
        keys = [k for k in dictionary.keys()]
        return keys

    def print_help(self):
        print('Select groups to include. Enter >> to start game.\n')
        print('Available groups:')
        print(str(self.dict_keys_to_list(self.flashcards.vocab_name_group)) + '\n')
        print('Active groups:')
        print(str(self.dict_keys_to_list(self.flashcards.active_groups)) + '\n')
        print('Available commands:')
        print('addall - adds all groups to active groups')
        print('rmall - removes all groups from active groups')
        print('add [group] - add one groups from active groups')
        print('rm [group] - remove one groups from active groups')
        print('>> - start the game')
        print('!! - quit')
        print('?? - display this message\n')

    def display(self):
        self.print_help()

        while True:
            

            user_input = input('[>] ')
            parse_input = user_input.partition(' ')

            print()

            if parse_input[0] == 'addall':
                print_success('Added all groups.\n')
                self.flashcards.active_groups = self.flashcards.vocab_name_group

            elif parse_input[0] == 'rmall':
                print_success('Removed all groups.\n')
                self.flashcards.active_groups = {}

            elif parse_input[0] == 'add':
                new_group = parse_input[2]
                if new_group == '':
                    print_input('Usage: add [group name]')
                elif not new_group in self.flashcards.vocab_name_group:
                    print_fail('Group not found\n')
                else:
                    key = new_group
                    value = self.flashcards.vocab_name_group[new_group]
                    self.flashcards.to_active(key, value)

            elif parse_input[0] == 'rm':
                key = parse_input[2]
                if key in self.flashcards.vocab_name_group:
                    self.flashcards.active_groups.pop(str(key))
                else:
                    print_fail('Group not found.\n')
           
            elif parse_input[0] == '>>':
                self.flashcards.set_state(self.flashcards.game_state)
            
            elif parse_input[0] == '??':
                self.print_help()
            
            elif parse_input[0] == '!!':
                print('Bye, bitch.')
                sys.exit(0)
            
            else:
                print_fail('Invalid command.')
                print()

            print_input('Available groups:')
            print_input(str(self.dict_keys_to_list(self.flashcards.vocab_name_group)) + '\n')
            print_input('Active groups:')
            print_input(str(self.dict_keys_to_list(self.flashcards.active_groups)) + '\n')


            # if len(user_input.split(' ')) == 1:
            #     if user_input == '>>':
            #         in_menu = False
            #         self.flashcards.set_state(self.flashcards.game_state)
            #     elif user_input == 'addall':
            #         stat.print_success('Added all groups.')
            #         self.flashcards.active_groups = self.flashcards.vocab_name_group
            #     elif user_input == 'removeall':
            #         stat.print_success('Removed all groups.')
            #         self.flashcards.active_groups = {}
            #     else:
            #         stat.print_fail('Invalid command.')

            # elif len(user_input.split(' ')) > 1:
            #     command, name = user_input.split(' ')
            #     if command == 'add':
            #         pass #TODO
            #     elif command == 'remove':
            #         pass #TODO
            #     else:
            #         stat.print_fail('Invalid command.')