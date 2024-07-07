import random

computer_choices = ['rock', 'paper', 'scissors']
valid_choices = ['rock', 'paper', 'scissors']


def get_user_choice():

  while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if user_choice in valid_choices:
      return user_choice
    else:
      print("Invalid choice. Please enter rock, paper, or scissors.")


def play_game(rounds):

  score = {'Wins': 0, 'Losses': 0, 'Ties': 0}
  for _ in range(rounds):
    computer_choice = random.choice(computer_choices)
    user_choice = get_user_choice()

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
      score['Ties'] += 1
      print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
      score['Wins'] += 1
      print("You win!")
    else:
      score['Losses'] += 1
      print("You lose!")

  return score


print('Lets play, rock paper, scissors. Start with choosing how many rounds you want to play.')

choice_round = int(input('Choose to play 3 or 5 rounds'))

if choice_round == 3:
    print('You have chosen 3 rounds.')
    rounds = choice_round
elif choice_round == 5:
    print('You have chosen 5 rounds.')
    rounds = choice_round
else:
    print('Invalid amount of rounds. Try again.')
    exit


final_score = play_game(rounds)


print(f"\nFinal Score:")
print(f"Wins: {final_score['Wins']}")
print(f"Losses: {final_score['Losses']}")
print(f"Ties: {final_score['Ties']}")

if final_score['Wins'] > final_score['Losses']:
  print("Congratulations! You won the game!")
elif final_score['Wins'] < final_score['Losses']:
  print("Better luck next time!")

        
        
