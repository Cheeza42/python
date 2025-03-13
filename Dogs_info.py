class Dog: # A general class about dogs, at first you'll have just the name and the age of the dog.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self): # Operation when we'll use print(MyDog...) will give only the name.
        return self.name 
        
    def getAge(self):# Operation when we'll use print(MyDog...) will give only the age.
        return self.age
  
    def __str__(self): # Operation when we'll use print(MyDog). will give you all the information you wrote.
        return f"Dog(Name: {self.name}, Age:{self.age})"

MyDog = Dog("buddy", 6) # Example of a general dog to run the code with. 

class Labrador(Dog): # A child class under "Dog" class, a breed named Labrador.
    def __init__(self, name, age, behavior, color): # Added some more information about this specific dog
        super().__init__(name, age) # A command that inheritate the data from the perent class
        self.behavior = behavior
        self.color = color
        
    def GetBehavior(self):
        return self.behavior
    
    def GetColor(self):
        return self.color
        
    def __str__(self):
        return f"Dog(Name:{self.name}, Age:{self.age}, Behavior:{self.behavior}, Color:{self.color})"
        
Dog2 = Labrador("Tyson", 7,"kind and sensetive", "white") # 2nd example of a specific dog under the general definition of "Dog"

print(Dog2)