#Paras chaudhary_202501100700103

# code starts...

from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self):
        print("\n----- PAYMENT RECEIPT -----")
        print(f"User Name       : {self.user_name}")
        print(f"Original Amount : ₹{self.original_amount}")
        print(f"Final Amount    : ₹{self.final_amount}")
        print("----------------------------\n")


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        
        gateway_fee = amount * 0.02
        gst = gateway_fee * 0.18
        
        self.final_amount = amount + gateway_fee + gst
        
        print("\nProcessing Credit Card Payment...")
        self.generate_receipt()


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback
        
        print("\nProcessing UPI Payment...")
        if cashback:
            print("Cashback Applied: ₹50")
        else:
            print("No Cashback Applied")
        
        self.generate_receipt()


# PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        
        international_fee = amount * 0.03
        conversion_fee = 20
        
        self.final_amount = amount + international_fee + conversion_fee
        
        print("\nProcessing PayPal Payment...")
        self.generate_receipt()


# Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount
        
        print("\nProcessing Wallet Payment...")
        
        if amount > self.balance:
            print("Transaction Failed: Insufficient Balance!")
            return
        
        self.balance -= amount
        self.final_amount = amount
        
        print(f"Remaining Wallet Balance: ₹{self.balance}")
        self.generate_receipt()


# Polymorphic Function
def process_payment(payment, amount):
    payment.pay(amount)


# ------------------ MAIN PROGRAM ------------------

user_name = input("Enter your name: ")
wallet_balance = float(input("Enter initial wallet balance: "))

wallet = WalletPayment(user_name, wallet_balance)

while True:
    print("\n===== PAYMENT MENU =====")
    print("1. Credit Card")
    print("2. UPI")
    print("3. PayPal")
    print("4. Wallet")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Thank you for using the system!")
        break

    amount = float(input("Enter amount to pay: "))

    if choice == 1:
        payment = CreditCardPayment(user_name)
    elif choice == 2:
        payment = UPIPayment(user_name)
    elif choice == 3:
        payment = PayPalPayment(user_name)
    elif choice == 4:
        payment = wallet
    else:
        print("Invalid choice! Try again.")
        continue

    process_payment(payment, amount)