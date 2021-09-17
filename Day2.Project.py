print("Welcome To The Tip Calculator ")

bill = input("What was the total bill? ")

tip = input("What percentage tip you would like to give? ")

people = input("How many people to split the bill?  ")

number = round (int(bill) / int(people) * (int(tip) / 100 + 1) )

print(f"Each person should pay: {number} ")
