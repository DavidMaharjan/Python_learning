class Atm:
    def __init__(self):
        self.pin = 0
        self.balance=0
        self.menu()
    #for displaying menu and taking user input   
    def menu(self):
        user_input= input("""
                          Hello How would you like to proceed
                          1. Enter 1 to Create a Pin
                          2. Enter 2 to Check Balance
                          3. Enter 3 to Withdraw
                          4. Enter 4 to Deposit
                          5. Enter 5 to Exit
                          """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.check_balance()
        elif user_input=="3":
            self.withdraw() 
        elif user_input=="4":
            self.deposit()
        else:
            print("exit")
    #for creating pin and storing it in the class variable
    def create_pin(self):
        self.pin=int(input("Enter your Pin: "))
        print("Pin created successfully")
      
    #for checking balance after verifying the pin    
    def check_balance(self):
        temp=int(input("Enter your Pin: "))
        if temp==self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Incorrect Pin")
    
    #for withdrawing amount after verifying the pin and checking if sufficient balance is available
    def withdraw(self):
        temp=int(input("Enter your Pin: "))
        if temp==self.pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<=self.balance:
                self.balance-=amount
                print(f"You have withdrawn {amount}. Your new balance is {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Incorrect Pin")
    
    #for depositing amount after verifying the pin
    def deposit(self):
        temp=int(input("Enter your Pin: "))
        if temp==self.pin:
            amount=int(input("Enter amount to deposit: "))
            self.balance+=amount
            print(f"You have deposited {amount}. Your new balance is {self.balance}")
        else:
            print("Incorrect Pin")
    

