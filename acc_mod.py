#Access Modifier

# class student:
#     def __init__(self):
#         self.name="Divyansh"
#         self._trade="AIPA"
#         self.__marks=90

#     def show_marks(self):
#         return self.__marks

# std=student()
# print(std.name)
# print(std._trade)
# print(std.show_marks())

# class Bank_Account:
#     def __init__(self,accountname,balance):
#         self.accountname=accountname
#         self.__balance=balance

#     def deposite(self,amount):
#         if amount >0:
#             self.__balance+= amount
#             print("Deposite successfull")
#         else:
#             print("Invalid amount")

#     def withdrawl(self,amount):
#         if amount <=0:
#             print("Invalid amount")

#         elif amount <=self.__balance:
#             self.__balance -= amount
#             print("Withdrawl successfull")
#         else:
#             print("Insufficient amount")

#     def check_balance(self):
#         print("current balance:",self.__balance)

# user=Bank_Account("Riya",1000)
# print(user.accountname)
# user.deposite(900)
# user.withdrawl(200)
# user.check_balance()


