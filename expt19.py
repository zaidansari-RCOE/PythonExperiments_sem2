'''
Title: Array Mathematics
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

import numpy as np

arr1 = np.array([[3, 6, 9], [12, 15, 18]])
arr2 = np.array([[2, 4, 6], [8, 10, 12]])

print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)

# Element-wise operations
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("\nElement-wise Addition:\n", addition)
print("\nElement-wise Subtraction:\n", subtraction)
print("\nElement-wise Multiplication:\n", multiplication)
print("\nElement-wise Division:\n", division)

vec1 = np.array([2, 3, 4])
vec2 = np.array([5, 6, 7])

dot_product = np.dot(vec1, vec2)
print("\nDot Product of vec1 and vec2:", dot_product)

cross_product = np.cross(vec1, vec2)
print("Cross Product of vec1 and vec2:", cross_product)

"""
Sample Output:

Array 1:
 [[ 3  6  9]
 [12 15 18]]

Array 2:
 [[ 2  4  6]
 [ 8 10 12]]

Element-wise Addition:
 [[ 5 10 15]
 [20 25 30]]

Element-wise Subtraction:
 [[ 1  2  3]
 [ 4  5  6]]

Element-wise Multiplication:
 [[ 6 24 54]
 [96 150 216]]

Element-wise Division:
 [[1.5 1.5 1.5]
 [1.5 1.5 1.5]]

Dot Product of vec1 and vec2: 56
Cross Product of vec1 and vec2: [-3  6 -3]
"""
