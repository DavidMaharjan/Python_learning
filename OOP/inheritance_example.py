class User :
    # def __init__(self,name,email):
    #     self.name = name
    #     self.email =email 
    
    def login(self):
        print("logged in successfully")
        
    def logout(self):
        print("logged out successfully")
    
    def register(self):
        print("registered successfully")

class Student(User):
    
    def enroll(self):
        print("enrolled successfully")
        
    def review(self):
        print("reviewed successfully")
        

class Instructor(User):
    
    def create_course(self ):
        print("course created successfully")
        
    def grade(self):
        print("graded successfully")
        
        
stu = Student()
stu.login()
stu.logout()
stu.register()
stu.enroll()
stu.review()
