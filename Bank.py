#CODE OF A BANK ACCOUNT

#IMPORT THE MATH LIBRARIES
import math

#CREATE AN CLASS AND NAME IT
class BankAccount:

#CREATING METHODS AND STATING THE PARAMETERS
    def __init__(self):
        self.balance=0

#CREATING A DEPOSIT METHOD 
    def deposit(self):
        Adeposit= int(input("Enter amount to be Deposited:"))
        self.balance+=Adeposit
        return math.trunc(Adeposit)
    
#WITHDRAW METHOD    
    def withdraw(self):
        amount= int(input("Enter the amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Insufficient Balance")
        else:
            print("\n Amount Withdrawn:", amount)
    
#CHECK BALANCE METHOD    
    def Check_balance(self):
        print("\n The Current Balance is:", self.balance)

#CUSTOMER DETAILS METHOD
    def Customer_details(self):
        Customer_name=input("Enter Customer Name:")
        print("Customer Name:", Customer_name)
        Account_no=int(input("Enter the Account Number:"))
        print("Account Number:",Account_no)
        Date_of_Opening=input("Enter Date Of Opening Account:")
        print("Date of Account Opening:", Date_of_Opening)
        print("Account Balance:",self.balance)

#OBJECT OF THE CLASS
Acdetail=BankAccount()

#CALLING THE FUNCTIONS WITH THE OBJECT OF THE CLASS
Acdetail.deposit()
Acdetail.withdraw()
Acdetail.Check_balance()
Acdetail.Customer_details()




