from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu_item = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What Would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
