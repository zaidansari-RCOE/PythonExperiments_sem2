'''
Title: Prime Number Checker
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    # Check for factors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    # If no factors found, the number is prime
    return True

# Input from user
num = int(input("Enter a number to check if it's prime: "))

# Check and display whether the number is prime
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

"""
Sample Output:

Enter a number to check if it's prime: 7
7 is a prime number.

Enter a number to check if it's prime: 10
10 is not a prime number.
"""
