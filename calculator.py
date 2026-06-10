"""Simple command-line calculator.

1. Ask the user which operation to perform
2. Take Num1 and Num2
3. Validate the selected option and perform the arithmetic operation
"""

print("welcome to asa's calculator!!!")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print("select an option below:\nA) Addition\nB) Subtraction\nC) Multiplication\nD) Division")

option = input("==> ").strip().upper()

if option in ("A", "a"):
    print(f"the sum of {num1} and {num2} is {num1 + num2}")
elif option in ("B", "b"):
    print(f"the difference of {num1} and {num2} is {num1 - num2}")
elif option in ("C", "c"):
    print(f"the product of {num1} and {num2} is {num1 * num2}")
elif option in ("D", "d"):
    if num2 == 0:
        print("Error: division by zero")
    else:
        print(f"the quotient of {num1} and {num2} is {num1 / num2}")
else:
    print("Invalid option selected.")

