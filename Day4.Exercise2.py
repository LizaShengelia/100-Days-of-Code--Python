import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

random_num = random.randint(0, len(names) - 1)

print(names[random_num])
