class Atm : 
    counter =1 
    def __init__(self):
        self.pin =""
        self.balance = 0
        self.sno=Atm.couter 
        Atm.counter += 1 
        self.menu()
    
    def menu(self):
        print(id(self))
        user_input = input("""
                           Welcome to the ATM Machine
                           Please choose from the following options:
                           1. Enter 1 to create a new pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           """)
        if user_input == "1":
            self.create_pin()  
        elif user_input == "2":
            self.deposit()
        elif user_input == "3": 
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you for using the ATM Machine")
            
        else:
            print("Invalid input, please try again")
             
    def create_pin(self):
           
            self.pin =input("Please enter a new pin:")
            print("pin created successfully")
        
            
    def deposit(self):
            user_pin = input("Please enter your pin:")
            if user_pin == self.pin:
                amount = int(input("Enter the amount to deposit:"))
                self.balance += amount
                print(f"You have deposited {amount}. Your new balance is {self.balance}")
            else:
                print("Invalid pin, please try again")
          
            
    def withdraw(self):
            user_pin = input("Please enter your pin:")
            if user_pin == self.pin:
                amount = int(input("Enter the amount to withdraw:"))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"You have withdrawn {amount}. Your new balance is {self.balance}")
                else:
                    print("Insufficient funds, please try again")
            else:
                print("Invalid pin, please try again")
            
    
    def check_balance(self):
            user_pin = input("Please enter your pin:")
            if user_pin == self.pin:
                print(f"Your current balance is {self.balance}")
            else:
                print("Invalid pin, please try again")
          
            
sbi = Atm()
