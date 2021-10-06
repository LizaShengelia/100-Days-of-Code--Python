from art import logo
from random import *

print(logo)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

guessed_number = randint(1,100)
print(f"Pss the number is {guessed_number}")

easy = 10
hard = 5

choose = input("Choose a difficulty. Type 'easy' or 'hard': ")

guess = int(input("Make a guess: ")) 

something = False

while not something:
  if choose == "easy"  and easy > 0:
      while guessed_number != guess:
          easy = easy - 1
          print("Guess again.")
          if guessed_number > guess:
            print("Too low")
            guess = int(input("Make a guess: "))
          elif guessed_number < guess:
            print("Too high")
            guess = int(input("Make a guess: "))
          print(f"You have {easy} attempts remaining to guess the number.")
      print("You out of attempts, you loose")
      something = True


  print(f"You got it! The answer was {guessed_number}.")


  
