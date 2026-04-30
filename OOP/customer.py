class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
    def intro(self):
        print(f"Hello, I am {self.name} and my gender is {self.gender}")
           
def greet(customer):
        print(id(customer))
        customer.name = "David"
        if customer.gender == "male":
            print(f"Hello {customer.name}, Sir")
        else:
            print(f"Hello {customer.name}, Ma'am")
        
        cust2 = Customer("Jane Doe","female")
        return cust2
cust = Customer("John Doe","female")
print(id(cust))

new_cust=greet(cust)
print(new_cust.name)

cust1=Customer("David","Male")
cust2=Customer("Kriti","Female")
cust3=Customer("Katrina","Female")

L= [cust1,cust2,cust3]
for i in L :
    print (i.intro())
    