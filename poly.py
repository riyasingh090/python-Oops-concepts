# class CashPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using cash")

# class UPIPayment:
#     def pay(self,amount):
#         print("paid",amount,"using UPI")

# class CardPayment:
#     def pay(self,amount):
#         print("paid",amount,"using card")

# class NetBanking:
#     def pay(self,amount):
#         print("paid",amount,"using NetBanking")

# payments=[
#     CashPayment(),
#     UPIPayment(),
#     CardPayment(),
#     NetBanking(),
# ]
# for payment in payments:
#     payment.pay(500)

# choise=input("choose payment method(cash/upi/card/netbanking):")
# if choise == "cash":
#     payment=CashPayment()
# elif choise == "upi":
#     payment= UPIPayment()
# elif choise == "card":
#     payment=CardPayment()
# elif choise == "NetBanking":
#     payment=NetBanking()
#     exit()


# payment.pay(1000)

class MobilePushNotification():
    def send(self,send_Notification):
        print("SendNotification",send_Notification,"MobilePushNotification")

class Email:
    def send(self,send_Notification):
        print("SendNotification",send_Notification,"Email")

class SMS:
    def send(self,send_Notification):
        print("SendNotification",send_Notification,"SMS")


choise=input("choose Notification Method(MobilePushNotification/Email/SMS):") 
if choise == "Mobile":
     send_Notification=MobilePushNotification()
elif choise == "SMS":
     send_Notification=SMS()
elif choise == "Email":
     send_Notification= Email()

send_Notification.send("Congratulation you got your parcel")
 
    