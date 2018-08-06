import re
import copy

class Vocab:
    group_name = ''
    vocab_list = {}

    def __init__(self, name = 'default name', vocab = {}):
        self.group_name = re.sub(r'^[[]|[]]$', '', name)
        # self.group_name = re.sub(r'[^a-z\s]', '', name)
        self.vocab_list = vocab

    def get_name(self):
        return copy.deepcopy(self.group_name)

    def get_vocab_list(self):
        return copy.deepcopy(self.vocab_list)

    def get_vocab_list_as_list(self):
        l = self.get_vocab_list()
        return list(l.items())

    def tostr(self):
        return self.group_name + '\n' + str(self.vocab_list)

    def check(self, word, guess):
        if not isinstance(word, str) or not isinstance(guess, str):
            return False
        if not word in self.vocab_list:
            return False
        return self.vocab_list[word] == guess

    def get_answer(self, word):
        return self.vocab_list[word]

    # I don't think this will ever be used but just in case
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.group_name = new_name

    def set_vocab_list(self, new_vocab_list):
        if not isinstance(new_vocab_list, dict):
            self.vocab_list = new_vocab_list

