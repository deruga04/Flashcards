import re
import copy

class Vocab:
    group_name = 'default name'
    vocab_list = []

    def __init__(self, name, vocab):
        group_name = name
        vocab_list = vocab

    def get_name():
        return copy.deepcopy(group_name)

    def get_vocab_list():
        return copy.deepcopy(vocab_list)

    # I don't think this will ever be used but just in case
    def set_name(new_name):
        group_name = new_name

    def set_vocab_list(new_vocab_list):
        vocab_list = new_vocab_list

