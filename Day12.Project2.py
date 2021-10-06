from art import logo
from random import randint

easy_level = 10
hard_level = 5

def check_answer(guess, guessed_number, turns):
  """checks answers and return turns"""
  if guessed_number > guess:
      print("Too low")
      return turns - 1
  elif guessed_number < guess:
      print("Too high")
      return turns - 1
  else:
      print(f"You got it! The answer was {guessed_number}.")

def difficulty():
 choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
 if choose == "easy":
   return easy_level
 else:
   return hard_level

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  guessed_number = randint(1,100)
  print(f"Pss the number is {guessed_number}")

  turns = difficulty()
  
  guess = 0

  while guess != guessed_number:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: ")) 

    turns = check_answer(guess, guessed_number, turns)  
    if turns == 0:
     print("You out of attempts, you loose")
     return
    elif guess != guessed_number:
     print("Guess again.")


game()

      

  
