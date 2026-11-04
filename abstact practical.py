
# Program to Calculate Area of Circle, Rectangle and Square
# Using Abstract Class and Inheritance

from abc import ABC, abstractmethod
import math


# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Circle Class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Rectangle Class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Square Class
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Creating Objects
c = Circle(5)
r = Rectangle(10, 4)
s = Square(6)


# Displaying Areas
print("Area of Circle =", round(c.area(), 2))
print("Area of Rectangle =", r.area())
print("Area of Square =", s.area())



# Exercise 2: Bank Account Using Abstract Class

from abc import ABC, abstractmethod


# Abstract Class
class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Savings Account Class
class SavingsAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited in Savings Account:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn from Savings Account:", amount)
        else:
            print("Insufficient Balance in Savings Account")

    def display_balance(self):
        print("Savings Account Balance:", self.balance)


# Current Account Class
class CurrentAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited in Current Account:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn from Current Account:", amount)
        else:
            print("Insufficient Balance in Current Account")

    def display_balance(self):
        print("Current Account Balance:", self.balance)


# Creating Objects
s = SavingsAccount(5000)
c = CurrentAccount(10000)


# Performing Operations
s.deposit(2000)
s.withdraw(1000)
s.display_balance()

print()

c.deposit(3000)
c.withdraw(2000)
c.display_balance()
