from .status_messages import *
from .vocab import Vocab
from .GameState import GameState
from .MenuState import MenuState
from .status_messages import *
from .vocab import Vocab
import sys
import re


class Flashcards:
    def __init__(self, args):
        self.game_state = GameState(self)
        self.menu_state = MenuState(self)
        self.state = self.menu_state

        self.verify_args(args)
        
        self.vocab = self.parse_files(args[1:])
        self.vocab_name_group = {vg.get_name():vg for vg in self.vocab}
        self.active_groups = {}

        self.state = self.menu_state
        self.state.display()

    def set_state(self, state):
        self.state = state
        self.state.display()

    def verify_args(self, args):
        try:
            if len(args) < 2:
                raise ValueError
            print_success('Yep, everything looks good.')
        except ValueError:
            print_warn('This script must be run with at least one vocabulary lists. Please view the documentation to learn how to create it.')
            print_warn('Usage: python3 flashcard.py filename [filenames]')
            print_warn('Example: python3 flashcard.py ~/vocab_list.txt ~/food.txt ~/fun.txt')
            sys.exit(0)

    def group_contains(self, vocab_groups):
        pass

    def parse_files(self, filenames):
        for filename in filenames:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    vocab_raw = file.read()
                    print_success('File ' + filename + ' found!')
                    print('Building vocabulary list...')
                    vocab_raw = vocab_raw.strip()
                    groups = re.split(r'\n{2,}', vocab_raw)

                    vocab_groups = []
                    for g in groups:
                        group_parse = g.split('\n')
                        group_name = group_parse[0]
                        group_list = {}

                        # print(group_name)

                        for p in group_parse[1:]:
                            # pair = re.split(r'(\b=\b|\s{1,}=\s{1,})', p)
                            pair = p.split('=')
                            # print(pair[0] + pair[1])
                            answer, translation = pair[0].strip(), pair[1].strip()
                            if answer in vocab_groups:
                                print_warn('Duplicate group name: ' + answer + '. Only the most recent entry will be entered.')

                            group_list[answer] = translation.strip()

                        vocab_groups.append(Vocab(group_name, group_list))

            except Exception as e:
                print_fail('File location ' + filename + ' not found. Please double-check the file name and make sure it exists.')

        return vocab_groups


    def to_active(self, key, value):
        self.active_groups[key] = value
