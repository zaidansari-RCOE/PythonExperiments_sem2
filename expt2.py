''' Title:Calculating Areas of Geometric Figures
    Name:Md. Zaid Mashooque Ansari
    Division:C
    UIN:241P057
    Roll no:51'''

import math
def art():
    b = int(input("Enter base of triangle:\n"))
    h = int(input("Enter height of triangle:\n"))
    return 0.5 * b * h
    
def arc():
    r = int(input("Enter radius of the circle:\n"))
    return math.pi*r*r
    
def arr():
    l = int(input("Enter length of rectangle:\n"))
    w = int(input("Enter breadth of rectangle:\n"))
    return w * l
    
n = int(input("\t\t*****Area Calculator*****\n\n1: Circle\n2: Triangle\n3: Rectangle\nEnter your choice: "))

if n == 1:
    print(f"Area of circle is {arc():.2f} units")

    
elif n == 2:
   print(f"Area of triangle is {art():.2f} units")
   
elif n == 3:
    print(f"Area of rectangle is {arr():.2f} units")
else:
    print("Enter a valid choice")

'''Output:
		*****Area Calculator*****

1: Circle
2: Triangle
3: Rectangle
Enter your choice: 1
Enter radius of the circle:
3
Area of circle is 28.27 units


		*****Area Calculator*****

1: Circle
2: Triangle
3: Rectangle
Enter your choice: 2
Enter base of triangle:
4
Enter height of triangle:
5
Area of triangle is 10.00 units

		*****Area Calculator*****

1: Circle
2: Triangle
3: Rectangle
Enter your choice: 3
Enter length of rectangle:
5
Enter breadth of rectangle:
6
Area of rectangle is 30.00 units'''
