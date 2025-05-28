num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
       result = int(num1) + int(num2)
    case "-":
        result = int(num1) - int(num2)
    case "*":
        result = int(num1) * int(num2)
    case "/":
        if int(num2) == 0:
            print("Cannot divide by zero.")
        else:
            result = int(num1) / int(num2)
print(f"The result is {result}.")
