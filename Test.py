# -*- coding: utf-8 -*-

#guess the number game

#ask player to guess the number
#establish a random query range
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0

    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        count += 1
   
        if guess < random_number:
            print("Sorry guess again too low.")
        
        elif guess > random_number:
            print("sorry, too high")
       
    print(f"congrats you guessed {random_number} correctly on attempt number {count}")        

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'{guess} is too high (H), too low (L), or correct (C)??')
        count += 1
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'yay the computer guessed {guess} correctly on count {count}')
    



computer_guess(1000)