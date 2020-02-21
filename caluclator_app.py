num1 = float(input("Please enter a number: "))
op = input("Please select a mathematical operation to perform: ")
num2 = float(input("Please select a second number: "))
op = input("Please select a mathematical operation to perform: ")



if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Syntax error")