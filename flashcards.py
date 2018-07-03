import random
import vocab as vocab
import sys

if len(sys.argv) != 2:
    print('This script must be run with a vocabulary list. Please view the documentation to learn how to create it.')
    print('Usage: python3 flashcard.py filename')
    print('Example: python3 flashcard.py ~/vocab_list.txt')
    sys.exit(0)



v = vocab.Vocab('hi', [])