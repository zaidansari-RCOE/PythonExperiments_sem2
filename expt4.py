''' Title:Exploring Basic Arithmetic Operations in Python
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''
# Basic Arithmetic Operations Program

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check if second number is not zero to avoid division/modulus error
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (modulus by zero)"

# Display the results
print("\n*** Arithmetic Operations Results ***")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")

'''Output:
Enter the first number: 10
Enter the second number: 3

--- Arithmetic Operations Results ---
Addition: 10.0 + 3.0 = 13.0
Subtraction: 10.0 - 3.0 = 7.0
Multiplication: 10.0 * 3.0 = 30.0
Division: 10.0 / 3.0 = 3.3333333333333335
Modulus: 10.0 % 3.0 = 1.0
'''
