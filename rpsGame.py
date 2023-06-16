# -*- coding: utf-8 -*

import random

def play():
    user = input("Lets play rock paper scissors.'r' for rock, 'p' for paper, and 's' for scissors. ready one, two, three shoot!!: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It is a tie'
    
    if winner(user, computer):
        return "you are a winner!!"
    
def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

print(play())


