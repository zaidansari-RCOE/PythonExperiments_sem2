'''Title: Number Type Identifier
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

def identify_number_type():
    n = int(input("Enter the number you want to check\n"))

    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

identify_number_type()

'''
Sample Output:

Enter the number you want to check
4
4 is even

Enter the number you want to check
7
7 is odd
'''

