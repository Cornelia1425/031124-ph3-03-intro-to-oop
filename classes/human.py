class Human:

    def __init__ (self:str, first_name:str, last_name:str):
        print("Building a new human")
        self.first_name = first_name
        self.last_name = last_name
        self._age= 0 #setting private value, because we don't want to run the age setter

    def __repr__ (self):
        return f"Human: {self.first_name} {self.last_name} Age: {self.age}"
    
    def say_full_name(self):
        return self.first_name + " " + self.last_name
    
    def happy_birthday(self):
        #why _, or it would trigger the ValueError
        self._age = self._age + 1  #can we self.age+1 here
        return self._age  #this is age setter
    
    #decorator
    @property 
    def age(self):
        return self._age #this is age getter
        
    @age.setter
    def age(self,value):
        # or Exception, general error #this is age setter
        raise ValueError ("Quit lying about your age!")
       
    
    

    