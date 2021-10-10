from art import logo, vs
from game_data import data
from replit import clear
import random
print(logo)



def check_answer(guess, a_score, b_score):
  if a_score > b_score:
    if guess == "a":
      return True
    else:
      return False
  else:
    if guess == "b":
      return True
    else:
      return False
    


def game():
  score = 0
  game_should_continue = True
  random2 = random.choice(data)
  
  while game_should_continue:
    random1 = random2
    random2 = random.choice(data)

    random1_all = random1['name'] + ',' + ' ' +  random1['description'] + ',' + ' ' + random1['country']

    random2_all = random2['name'] + ',' + ' ' +  random2['description'] + ',' + ' ' + random2['country']


    print(f"Compare A: {random1_all}")

    print(vs)

    print(f"Against B: {random2_all}")


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_score = random1['follower_count']
    b_score = random2['follower_count']

    is_correct = check_answer(guess, a_score, b_score)

    clear()
    print(logo)
    
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")


game()
