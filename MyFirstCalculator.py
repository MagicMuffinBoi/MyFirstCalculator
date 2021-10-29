import time

print("<!><!><!><!><!> PythonCalculator <!><!><!><!><!>")
time.sleep(0.2)
print("This calculator can subtract, multiply, devide, and add")
time.sleep(0.3)
print("Select an operation to perform: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

userchooseoperation = input()

# If the user chose 1
if userchooseoperation == "1":
    number1 = input("Input your first number: ")
    time.sleep(0.2)
    number2 = input("Input your second number: ")
    print("Your answer is: " + str(int(number1) + int(number2)))

# If the user chose 2
elif userchooseoperation == "2":
    number1 = input("Input your first number: ")
    time.sleep(0.2)
    number2 = input("Input your second number: ")
    print("Your answer is: " + str(int(number1) - int(number2)))

# If the user chose 3
elif userchooseoperation == "3":
    number1 = input("Input your first number: ")
    time.sleep(0.2)
    number2 = input("Input your second number: ")
    print("Your answer is: " + str(int(number1) * int(number2)))

# If the user chose 4
elif userchooseoperation == "4":
    number1 = input("Input your first number: ")
    time.sleep(0.2)
    number2 = input("Input your second number: ")
    output4 = str(int(number1) / int(number2))
    print("Your answer is: " + str(int(number1) / int(number2)))
else:
    print("That is not an option.")