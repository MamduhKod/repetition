

import random


def guesses(guess):
    if guess > 100:
     print('Your guess is too high, try again.')
     return False
    elif guess <1:
     print('Your guess is too low, trye again.')
     return False
    else:
        print(f'Your guess is {guess}.')
    

guess = int(input('Guess a number, from 1-100:'))
guesses(guess)
random_number = random.randint(1,100)

guess_count = 0

while guess_count < 5:
    if guess < random_number:
        print('Your number is too low, guess again.')
        guess_count +=1
        guess = int(input('Guess again'))
        guesses(guess)
    if guess > random_number:
        print('Your number is too high, guess again.')
        guess_count +=1
        guess = int(input(('Guess again')))
        guesses(guess)
    if guess_count == 5:
        print('Too many guesses')
    else:
        print('You have correctly guessed ',guess)
        break
    


    

