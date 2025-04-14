''' Title:Calculating Gross Salary of an Employee
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''
def gs():
    # Print the title
    print("*** GROSS SALARY CALCULATOR ***\n")

    # Get the basic salary from the user
    bs = float(input("Enter the basic salary: "))

    # Calculate allowances
    da = bs * 0.70  # Dearness Allowance (70% of basic)
    ta = bs * 0.30  # Travel Allowance (30% of basic)
    hra = bs * 0.10  # House Rent Allowance (10% of basic)

    # Calculate gross salary
    gross_salary = bs + da + ta + hra

    # Display the gross salary
    print(f"\nGross Salary = {gross_salary}")

# Call the function to run the program
gs()

'''Output:
*** GROSS SALARY CALCULATOR ***

Enter the basic salary: 50000

Gross Salary = 105000.0
'''
