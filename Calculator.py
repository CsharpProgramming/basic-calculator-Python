print("Welcome to my Calculator")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

method = input("Enter operation name (+, -, *, /): ")

if method == "+":
    print(str(int(num1) + int(num2)))

elif method == "-":
    print(str(int(num1) - int(num2)))

elif method == "*":
    print(str(int(num1) * int(num2)))

elif method == "/":
    print(str(int(num1) / int(num2)))

else:
    print("Wrong operation name")
