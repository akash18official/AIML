class MyProfile:
    def __init__(self,name='Akash',age='29'):
        self.name=name
        self.age=age

    def viewprofile(self):
        prof=f"my name is {self.name} and i'm {self.age} years old"
        return prof
        
