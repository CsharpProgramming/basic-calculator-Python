print("Welcome to my Calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

method = input("Enter operation name (+, -, *, /): ")

if method == "+":
    print(num1 + num2)

elif method == "-":
    print(num1 - num2)

elif method == "*":
    print(num1 * num2)

elif method == "/":
    print(num1 / num2)

else:
    print("Wrong operation name")
