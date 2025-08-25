class User():
    def __init__(self,first_name,last_name,email,contact,age):

        # public instance/object attributes
        self.first_name = first_name
        self.last_name =last_name
        self.email= email
        self.contact = contact
        # private instance/object attribute
        self._age =age
    
    def get_age(self):
        return self._age
    def set_age(self,new_age):
        if (new_age<=0) or (new_age>=60) : 
            print("Invalid Age")
        else:
            self._age = new_age
    
    
    def describe_user(self):
        print(f"""
               {self.first_name} {self.last_name}
               {self.email}
               {self.contact}
               """)
    def greet_user(self):
        print(f"""
              Mr. {self.first_name} {self.last_name}, you are welcome to my portal""")
class Student:
    pass
class Teacher:
    pass