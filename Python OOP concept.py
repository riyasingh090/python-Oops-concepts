# class aipa:
#     def __init__(self,name,roll_no,trade,marks): #Constructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks

# std1=aipa("Riya",1,"AIPA",75)
# std2=aipa("Divyansh",2,"AIPA",85)
# print(std1.name)
# print(std1.roll_no)
# print(std1.trade)
# print(std1.marks)


# print(std2.name)
# print(std2.roll_no)
# print(std2.trade)
# print(std2.marks)


# class Student:
#     def __init__(self,name,roll_no,trade,marks): #Constructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks


#     def display_details(self):
#         print("Name:",self.name)
#         print("Roll:",self.roll_no)
#         print("Trade:",self.trade)
#         print("Marks:",self.marks) 

#     def check_result(self):
#         if self.marks >=40:
#             print("pass")
#         else:
#             print("Fail")


#     def percentage(self,total_marks):
#         return (self.marks/total_marks)*100

        
# student1=Student("Riya",1,"AIPA",75)
# student2=Student("Divyansh",2,"AIPA",85)

# student1.display_details()
# student1.check_result()

# student2.display_details()
# student2.check_result()


class Car:

    def __init__(self,brand,price,speed,seet):
        self.brand=brand
        self.price=price
        self.speed=speed
        self.seet=seet


    def display_details(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Speed:",self.speed)
        print("Seet:",self.seet)

    def check_speed(self):
        if self.speed >=150:
            print("Too fastest")

        elif self.speed <=150:
            print("Average")

        else :
            print("this is a cycle")

car1=Car("BMW",25000000,100,6)
car2=Car("Thar",2000000,95,6)

car1.display_details()
car1.check_speed()

car2.display_details()
car2.check_speed()

