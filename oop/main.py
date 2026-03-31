class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speak()
        
    def speak(self):
        print("animal is speaking")
        
class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type
        self.speak()
    
    def speak(self):
        print("bark")
    
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.speak()
        self.jump()
    
    def speak(self):
        print("meow")
    
    def jump(self):
        print("cat jumping")

class Bird(Animal):
    def __init__(self, name, age,):
        super().__init__(name, age)
        self.fly = True
        self.speak()
        self.fly()
        
    def speak(self):
        print("tweet")
    
    def fly(self):
        print("bird is flying")
        
class Fish(Animal):
    def __init__(self, name, age, water_type ):
        super().__init__(name, age)
        self.water_type = water_type
        self.speak()
        self.swim()
        
    def speak(self):
        print("blab")
    
    def swim(self):
        print("fish swims")
    
class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed
        self.speak()
        self.sprint()
        
    def speak(self):
        print("yeeh")
    
    def sprint(self):
        print("horse running")
        
caesar = Dog("caesar", 24, "chitsu")
    