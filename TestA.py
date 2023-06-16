# -*- coding: utf-8 -*

import random

def play():
    user = input(" What is your choice?? 'r' for rock, 'p' for paper, and 's' for scissors.\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'tie'
    
    if is_winner(user, computer):
        return 'You Won!'
    
    return 'You lost!'
    
def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') \
    or (player == 'p' and opponent == 'r'):
        return True
    


print(play())