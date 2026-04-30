class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self,new_street,city,state):
        self.address.change_address(new_street,city,state)

class Address : 
    def __init__(self,street,city,state):
        self.street = street
        self.city = city
        self.state = state
        
    def change_address(self,street,city,state):
        self.street = street
        self.city = city
        self.state = state

address=Address("123 Main St","Anytown","Anystate")        
customer1 = customer("John Doe","Male",address)        
        
print(customer1.address.street)

customer1.edit_profile("456 Elm St","Othertown","Otherstate")
print(customer1.address.street)