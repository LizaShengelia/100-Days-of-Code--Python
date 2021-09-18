print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")

extra_cheese = input("Do you want extra cheese? Y or N ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

bill = 0

if size == "S":
  bill = 15
  #print("Your final bill is: $15")
  if add_pepperoni == "Y":
    bill += 2


elif size == "M":
  bill = 20
  #print("Your final bill is: $20")
  if add_pepperoni == "Y":
   bill += 3


else:
  bill = 25
  #print("Your final bill is: $25")
  if add_pepperoni == "Y":
   bill += 3

if extra_cheese == "Y":
 bill += 1
 print(f"Your final bill is: ${bill}")
    


 

  






