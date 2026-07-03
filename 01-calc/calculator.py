first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        result = "can't divide by 0 dummy"
    else: 
        result = first_number / second_number
else:
    result = "huh?"

print(f"your number is: {result}")