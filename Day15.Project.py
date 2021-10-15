MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarter = 0.25
dimes = 0.10
nickles = 0.05
penny = 0.01
game = True

while game:
    answer = input(" What you like? (espresso/latte/cappuccino): ")
    if answer == "off":
       game = False
       break

    if answer == "report":
        print(resources)


    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if answer == "cappuccino" and resources["water"] < 250 or resources["milk"] < 100 or resources["coffee"] <= 24:
          print("Sorry there is not enough water")

        elif answer == "espresso" and resources["water"] < 50 or resources["coffee"] <= 18:
          print("Sorry there is not enough coffe")

        elif answer == "latte" and resources["water"] < 200 or resources["coffee"] <= 24 or resources["milk"] < 150:
          print("Sorry there is not enough milk")
    else:
        game = True

    print("Please insert coins.")

    quarter_number = int(input("how many quarters?: "))

    dimes_number = int(input("how many dimes: "))

    nickles_number = int(input("how many nickles: "))

    penny_number = int(input("how many penny: "))


    calculate = quarter * quarter_number + dimes * dimes_number + nickles * nickles_number + penny * penny_number

    if answer == "espresso" and calculate < 1.5:
        print("Sorry that's not enough money. Money refunded.")
    elif answer == "espresso" and calculate > 1.5:
        change = calculate - 1.5
        change = str(round(change, 2))
        print(f"Here is {change} in change.")
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        resources["money"] = 1.5
    elif answer == "espresso" and calculate == 1.5:
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        resources["money"] = calculate

    if answer == "latte" and calculate < 2.5:
        print("Sorry that's not enough money. Money refunded.")
    elif answer == "latte" and calculate > 2.5:
        change = calculate - 2.5
        change = str(round(change, 2))
        print(f"Here is {change} in change.")
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100
        resources["money"] = 2.5
    elif answer == "latte" and calculate == 2.5:
        resources["water"] = resources["water"] - 200
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 100
        resources["money"] = calculate


    if answer == "cappuccino" and calculate < 3.0:
        print("Sorry that's not enough money. Money refunded.")
    elif answer == "cappuccino" and calculate > 3.0:
        change = calculate - 1.5
        change = str(round(change, 2))
        print(f"Here is {change} in change.")
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150
        resources["money"] = 3.0
    elif answer == "cappuccino" and calculate == 3.0:
        resources["water"] = resources["water"] - 250
        resources["coffee"] = resources["coffee"] - 24
        resources["milk"] = resources["milk"] - 150
        resources["money"] = calculate

    print(resources)
    print(f"Here is your {answer} ☕️. Enjoy!")
