'''
Title: Simple Calculator Using Functions
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

print("***CALCULATOR***\n")

# Input from the user
a = int(input("Enter number a: \n"))
b = int(input("Enter number b: \n"))
c = int(input("Enter choice for operation:\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Modulus\n"))

# Define the functions for each operation
def add():
    sum = a + b
    print(f"Addition of {a} & {b} is {sum}")

def sub():
    diff = a - b
    print(f"Subtraction of {a} & {b} is {diff}")

def mult():
    prod = a * b
    print(f"Multiplication of {a} & {b} is {prod}")

def div():
    if b == 0:  # Check for division by zero
        print("Error: Division by zero is not allowed.")
    else:
        divi = a / b
        print(f"Division of {a} & {b} is {divi}")

def mod():
    modul = a % b
    print(f"Modulus of {a} & {b} is {modul}")

# Perform the chosen operation based on user input
if c == 1:
    add()
elif c == 2:
    sub()
elif c == 3:
    mult()
elif c == 4:
    div()
elif c == 5:
    mod()
else:
    print("Invalid choice, exiting the program.")

"""
Sample Output:

***CALCULATOR***

Enter number a: 
5
Enter number b: 
3
Enter choice for operation:
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Modulus
1
Addition of 5 & 3 is 8

Enter number a: 
10
Enter number b: 
2
Enter choice for operation:
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Modulus
4
Division of 10 & 2 is 5.0

Enter number a: 
10
Enter number b: 
0
Enter choice for operation:
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Modulus
4
Error: Division by zero is not allowed.
"""
