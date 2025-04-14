'''
Title: Phone Number and Email ID Validator
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

import re

# Regex patterns
phone_pattern = re.compile(r'^\+?[0-9]{10,15}$')  # Accepts digits, optional '+' at start
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')  # Basic email validation

# Input from user
phone = input("Enter your phone number (with or without country code): ")
email = input("Enter your email ID: ")

# Validate phone
if phone_pattern.match(phone):
    print("✅ Phone number is valid.")
else:
    print("❌ Invalid phone number format.")

# Validate email
if email_pattern.match(email):
    print("✅ Email ID is valid.")
else:
    print("❌ Invalid email ID format.")
  
"""
Sample Output 1:
Enter your phone number (with or without country code): +919876543210
Enter your email ID: example@example.com
✅ Phone number is valid.
✅ Email ID is valid.

Sample Output 2:
Enter your phone number (with or without country code): 9876543210
Enter your email ID: invalid-email
❌ Invalid phone number format.
❌ Invalid email ID format.
"""
