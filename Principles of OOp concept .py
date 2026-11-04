# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary
#     def inc_salary(self,amount):
#         if amount >0:
#             self.__salary += amount
#             print("salary updated")
#         else:
#             print("invalid amount")

# emp=Employee("Riya",25,50000)
# print("salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Blance:",emp.get_salary())

# Inheritence

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d=Dog()
# d.property()
# d.bark()

# MUltiple Inheritence
# class Father():
#     def skill1(self):
#         print("Driving")


# class Mother():
#     def skill2(self):
#         print("Cooking")


# class Child(Father,Mother):
#     def Qualities(self):
#         print("Inherited Skills from Parentys:")

# x=Child()
# x.Qualities()
# x.skill1()
# x.skill2()

# Multi Level Inheritence

# class Grandfather():
#     def house(self):
#         print("Grandfather's house")

# class Father (Grandfather):
#     def bike(self):
#         print("Father's bike")

# class Son(Father):
#     def laptop(self):
#         print("Son's laptop")

# s=Son()
# s.house()
# s.bike()
# s.laptop()

# Hierarchical inheritance

# class Institute():
#     def name(self):
#         print("NSTIW Allahabad")

# class Teacher(Institute):
#     pass

# class Student(Institute):
#     pass

# class Housekeeping(Institute):
#     pass

# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name()

# class Grandfather():
#     def house(self):
#         print("Grandfather's house")

# class Father(Grandfather):
#     def bike(self):
#         print("Father's bike")

# class Son(Grandfather):
#     def laptop(self):
#         print("son's Laptop")

# class Grandson(Father,Son):
#     def car(self):
#         print("Grandson's car")

# g=Grandson()
# g.house()
# g.bike()
# g.laptop()
# g.car()