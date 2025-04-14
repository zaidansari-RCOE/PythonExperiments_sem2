'''
Title: OOPS Implementation in Python
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

# Base class
class Animal:
    def __init__(self, name):
        """Constructor to initialize the animal's name."""
        self.name = name

    def speak(self):
        """Base method to return animal sound (to be overridden)."""
        return "Animal sound"

# Derived class 1 - Dog
class Dog(Animal):
    def speak(self):
        """Override the speak method for Dog."""
        return "Woof!"

# Derived class 2 - Cat
class Cat(Animal):
    def speak(self):
        """Override the speak method for Cat."""
        return "Meow!"

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Display the result
print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")

'''
Sample Output:
Buddy says Woof!
Whiskers says Meow!
'''
