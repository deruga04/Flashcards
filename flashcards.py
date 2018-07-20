import random as rand
import vocab as vocab
import sys
import status_messages as stat
import re
import traceback

vocab_groups = []

def verify_args(args):
    try:
        if len(args) < 2:
            raise ValueError
        stat.print_success('Yep, everything looks good.')
    except ValueError:
        stat.print_warn('This script must be run with at least one vocabulary lists. Please view the documentation to learn how to create it.')
        stat.print_warn('Usage: python3 flashcard.py filename [filenames]')
        stat.print_warn('Example: python3 flashcard.py ~/vocab_list.txt ~/food.txt ~/fun.txt')
        sys.exit(0)

def group_contains(vocab_groups):
    pass

def parse_files(filenames):
    for filename in filenames:
        try:
            file = open(filename, 'r', encoding='utf-8')
            vocab_raw = file.read()
            stat.print_success('File ' + filename + ' found!')
            print('Building vocabulary list...')
            vocab_raw = vocab_raw.strip()
            groups = re.split(r'\n{2,}', vocab_raw)

            for g in groups:
                group_parse = g.split('\n')
                group_name = group_parse[0]
                group_list = {}

                # print(group_name)

                for p in group_parse[1:]:
                    # pair = re.split(r'(\b=\b|\s{1,}=\s{1,})', p)
                    pair = p.split('=')
                    group_list[pair[0].strip()] = pair[1].strip()


                vocab_groups.append(vocab.Vocab(group_name, group_list))


        except Exception as e:
            stat.print_fail('File location ' + filename + ' not found. Please double-check the file name and make sure it exists.')
            print(traceback.format_exc())

    return vocab_groups

def display_game(groups):
    user_input = ''
    stat.print_input('Welcome! The vocab game will now start. You can quit any time by entering !! into the console.')
    while user_input != '!!':
        group = rand.choice(groups)
        word = rand.choice(list(group.get_vocab_list().keys()))
        user_input = input(word + ': ')
        if group.check(word, user_input):
            stat.print_success('Correct!')
        elif user_input == '!!':
            pass
        else:
            stat.print_fail('So close! The correct word was ' + group.get_answer(word))

# for tmp in vocab_groups:
#     print(tmp.tostr())

# new_group = ''
# while new_group != '!quit':
#     active_groups = []
#     

def init(args):
    verify_args(args)
    vocab_groups = parse_files(args[1:])
    # vocab_group_names = list(map(lambda x: x.get_name(), vocab_groups))
    vocab_name_group = {vg.get_name():vg for vg in vocab_groups}
    display_game(vocab_groups)