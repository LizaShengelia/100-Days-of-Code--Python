import random
from replit import clear
from art import logo

def deal_card():
  """return random car from deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10, 10, 10]
  item = random.choice(cards)
  return item
deal_card()


def calculate_score(cards):
  """ Take a list of cards and calculates it """
  if sum(cards) == 21 and len(cards) == 2:
   return 0
  if sum(cards) > 21 and 11 in cards:
      cards.remove(11) 
      cards.append(1)
  return sum(cards)

def play():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False 

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards} {user_score}")
    print(f"computer first card: {computer_cards[0]}")


    if user_score == 0 or user_score > 21 or computer_score == 0:
      is_game_over = True 
    else:
      ask = input("Do you want another card? say 'y' or 'n' ")
      if ask == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  #def calculate_score(l):
  # total = 0
    #for val in l:
    #  total = total + val
  # return total
  #print(calculate_score(user_cards))

  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("its a draw")
      is_game_over = True
    elif computer_score == 0:
      print("you lost")
      is_game_over = True
    elif user_score == 0:
      print("you won")
      is_game_over = True
    elif user_score > 21:
      print("you lost")
      is_game_over = True
    elif computer_score > 21:
      print("you won")
      is_game_over = True
    elif computer_score > user_score:
      print("you lost")
      is_game_over = True
    elif user_score > computer_score:
      print("you won")
      is_game_over = True




  print(f"  your final hand: {user_cards}, Final score: {user_score}")
  print(f"  computer final hand:  {computer_cards}, Final score: {computer_score}")
  compare(user_score, computer_score)

    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()
