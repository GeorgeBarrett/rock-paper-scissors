import random

def play():
    user = input("'r' for rock, 'p' for paper, and 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie'