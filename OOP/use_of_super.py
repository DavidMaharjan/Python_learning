"""
This module contains examples of the use of super() in Python classes.
Super() is a built-in function that allows you to call methods from a parent class in a child class. It is commonly used in object-oriented programming to ensure that the parent class's methods are properly called and to avoid code duplication.
"""

class Phone:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
class SmartPhone(Phone):
    def __init__(self,brand,model,os,ram):
        super().__init__(brand,model)
        self.__os = os
        self.__ram = ram
        
    def get_os(self):
        return self.__os
    
    def get_ram(self):
        return self.__ram
    
    def change_model(self,new_model):
        super().__init__(self.get_brand(),new_model)
        
phone1 = SmartPhone("Apple","iPhone 12","iOS",4)
print(phone1.get_brand()) # Output: Apple
    

