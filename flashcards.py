import random
import vocab as vocab
import sys
import status_messages as stat
import re

vocab_groups = []


if len(sys.argv) < 2:
    stat.print_warn('This script must be run with at least one vocabulary lists. Please view the documentation to learn how to create it.')
    stat.print_warn('Usage: python3 flashcard.py filename [filenames]')
    stat.print_warn('Example: python3 flashcard.py ~/vocab_list.txt ~/food.txt ~/fun.txt')
    sys.exit(0)

filename = sys.argv[1]

try:
    file = open(filename, 'r')
    vocab_raw = file.read()
except:
    stat.print_fail('File location ' + ' not found. Please double-check the file name and make sure it exists.')
    sys.exit(0)

stat.print_success('File ' + filename + ' found!')
print('Building vocabulary list...')

vocab_raw = vocab_raw.strip()
groups = re.split(r'\n{2,}', vocab_raw)

for g in groups:
    group_parse = g.split('\n')
    group_name = group_parse[0]
    group_list = []

    for p in group_parse[1:]:
        pair = re.split(r'(\b=\b|\s{1,}=\s{1,})', p)
        group_list.append((pair[0], pair[2]))

    vocab_groups.append(vocab.Vocab(group_name, group_list))

for tmp in vocab_groups:
    print(tmp.tostr())

# new_group = ''
# while new_group != '!quit':
#     active_groups = []
#     