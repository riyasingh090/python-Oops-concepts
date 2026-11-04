# from abc import ABC,abstractmethod

# class Payment(ABC): # parent abstract class
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class Cash(Payment):
#     def pay(self,amount):
#         print("paid",amount,"using Cash")

# class UPI(Payment):
#     def pay(self,amount):
#         print("paid",amount,"using UPI")

# class DebitCard(Payment):
#     def pay(self,amount):
#         print("paid",amount,"using DebitCard")

# class Cheque(Payment):
#     def pay(self,amount):
#         print("paid",amount,"using Cheque")

# class NetBanking(Payment):
#     def pay(self,amount):
#         print("paid",amount,"using NetBanking")

# p1=UPI()
# p1.pay(5000)

# p2=Cash()
# p2.pay(500)

# p4=DebitCard()
# p4.pay(2000)

# p5=Cheque()
# p5.pay(50000)

# p6=NetBanking()
# p6.pay(9000)

# print("2.] Practice")
# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass

# class Bike(Vehicle):
#     def drive(self):
#         print("Bike is moving")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is moving")

# class Bus(Vehicle):
#     def drive(self):
#         print("Bus is moving")

# class Cycle(Vehicle):
#     def drive(self):
#         print("Cycle is moving")

# car=Car()
# bike=Bike()
# bus=Bus()
# cycle=Cycle()
# car.drive()
# bike.drive()
# bus.drive()
# cycle.drive()

