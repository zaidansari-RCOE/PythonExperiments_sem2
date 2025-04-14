'''
Title: Basic Exception Handling
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

def Division():
    #Performs division with exception handling.
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    Division()

"""
Sample Output:

Enter the numerator: 10
Enter the denominator: 2
Result: 5.0
Execution completed.

Enter the numerator: 10
Enter the denominator: 0
Error: Division by zero is not allowed.
Execution completed.

Enter the numerator: abc
Enter the denominator: 2
Error: Invalid input! Please enter numeric values.
Execution completed.
"""
