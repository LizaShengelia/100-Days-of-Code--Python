total = 0 
for number in range(1, 101):
 if(number % 5 != 0 and number % 3 != 0):
   total = number
   print(total)
 if(number % 3 == 0 and number % 5 != 0):
   print("Fizz")
 if(number % 5 == 0 and number % 3 != 0):
   print("Buzz")
 if(number % 3 == 0 and number % 5 == 0):
   print("FizzBuzz")


