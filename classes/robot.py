class Robot:

    #magic/ dunder method
    def __init__(self:str,name:str, color:str, operating_system:str):
        print("Building a new robot")
        self.name = name
        self.color = color
        self.operating_system = operating_system

    def __repr__ (self):
        return f"name={self.name} color={self.color} operating_system={self.operating_system}"
    

    def this_is_self(self):
        return self
    
    def say_hello(self):
        return "hello"
    
    def kill(self):
        return "MURDER"
    
    @property
    def name(self):
        #return "I AM A PROPERTY"
        return self._name.lower()
    
    #getter and setter variable
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def operating_system(self):
        #return "I AM A PROPERTY"
        return self._operating_system.upper()
    
    @operating_system.setter
    def operating_system(self, value):
        if type(value) == str:
            self._operating_system=value
        else:
            raise TypeError("Robot operating system must be a string")
    
   
    