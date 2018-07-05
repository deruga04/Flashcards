import re
import copy

class Vocab:
    group_name = 'default name'
    vocab_list = []

    def __init__(self, name, vocab):
        self.group_name = re.sub(r'[^a-z\s]', '', name)
        self.vocab_list = vocab

    def get_name(self):
        return copy.deepcopy(group_name)

    def get_vocab_list(self):
        return copy.deepcopy(vocab_list)

    def tostr(self):
        return self.group_name + '\n' + str(self.vocab_list)

    # I don't think this will ever be used but just in case
    def set_name(self, new_name):
        group_name = new_name

    def set_vocab_list(self, new_vocab_list):
        vocab_list = new_vocab_list