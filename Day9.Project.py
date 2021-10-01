from replit import clear

from art import logo 
print(logo) 

names = {}
biding = False

def find_highest_bidder(names):
  bid_highest = 0
  winner = ""
  for bidder in names:
    bit_amount = names[bidder]
    if bit_amount > bid_highest:
     bid_highest = bit_amount
     winner = bidder

  print(f"Winner is {winner} with {bid_highest}$ points")


while not biding:
  Name = input("Whats our name? ")

  Bid = int(input("Whats your bid price? $"))

  names[Name] = Bid

  question = input("Are there others users who wants to bid? Type 'Yes' or 'no' ")
  if question == "no":
    biding = True
    find_highest_bidder(names)
    #max_key = max(names, key=names.get)
    #print(f"{max_key}is Winner")

  else:
    clear()
