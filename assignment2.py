import random

random_number = random.randint(1, 100)

while True:
  guess = int(input("Guess a random number between 1 and 100: "))

  if guess > random_number:
    print("Lower!")
  elif guess < random_number:
    print("Higher!")
  else:
    print("Congratulations! You guessed the number", random_number)
    break 

print("Thanks for playing!")




    