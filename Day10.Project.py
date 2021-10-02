from art import logo
#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2


operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide
}


def calculator():
  print(logo)

  num1 = float(input("What is first number?: "))

  for math in operations:
    print(math)

  operation_symbol = input("Pick an operation from this line above: ")

  num2 = float(input("What is next number?: "))

  answer1 = operations[operation_symbol](num1, num2)

  final_num = print(f"{num1} {operation_symbol} {num2} = {answer1}")


  question = input(f"Type 'y' to continue calculating with {answer1} or type 'n' to exit: ")

  should_continue = True


  while should_continue:
    num3 = float(input("What is next number?: "))
    operation_symbol = input("Pick another operation from this line above: ")
    answer2 = operations[operation_symbol](answer1, num3)
    print(f"{answer1} {operation_symbol} {num3} = {answer2}")
    question = input(f"Type 'y' to continue calculating with {final_num} or type 'n' to exit: ")
    if question == 'y':
      answer1 = answer2
    else:
      should_continue = False
      calculator()
  

calculator()
