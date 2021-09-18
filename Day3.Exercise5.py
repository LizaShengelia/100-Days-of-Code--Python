print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

all = name1 + name2

lower_case_all = all.lower()
 
t = lower_case_all.count("t")
r = lower_case_all.count("r")
u = lower_case_all.count("u")
e = lower_case_all.count("e")

l = lower_case_all.count("l")
o = lower_case_all.count("o")
v = lower_case_all.count("v")
e = lower_case_all.count("e")

a = t + r + u + e 
b = l + o + v + e

every = (str(a) + str(b))

if 90 < int(every) < 10:
  print(f"Your score is {every}, you go together like coke and mentos.")
elif 40 < int(every) < 50:
  print(f"Your score is {every}, you are alright together.")
else:
  print(f"Your score is {every}.")

