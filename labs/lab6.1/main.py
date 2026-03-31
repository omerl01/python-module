class Person:
    def __init__(self, name, age, city, job):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        
    def introduction(self):
        print(f"name: {self.name}, age: {self.age}, city: {self.city}, job: {self.job}")
        
    

# person1 = Person("omer", 24, "Hadera", "Devops")
# person1.introduction()

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def show_car(self):
        print(f"brand: {self.brand}, model: {self.model}, year: {self.year}, color: {self.color}")
        
chevi = Car("chevrollete", "spark", 2017, "black")
# chevi.show_car()

class Book():
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages= pages
        self.genre = genre
    
    def show_book(self):
        print(self.title, self.genre)
    
notebook = Book("meditations", "marcus aurelius", 345, "philosopy")

# notebook.show_book()

class Dog:
    def __init__(self, name, age, breed, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight
    
    def show_dog(self):
        print(self.name, self.age, self.breed, self.weight)


ceaser = Dog("caesar", 9, "chitzu", 5)
# ceaser.show_dog()

class Phone:
    def __init__(self, brand, model, price, battery):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = battery
    
    def show(self):
        print(self.price)
iphone = Phone("ipone", 12, 2300, 80)
# iphone.show()


class Student:
    def __init__(self, name , age, grade, school):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    
    def show(self):
        print(self.name, self.grade)
        
omer = Student("omer", 24, 100, "iitc")
# omer.show()

class Movie:
    def __init__(self, title, year, rating, duration):
        self.title = title
        self.year= year
        self.rating = rating
        self.duration = duration
    
    def show(self):
        print(self.rating)
        
apes = Movie("planet ofthe apes", 2000, 5, 130)
# apes.show()

class Laptop:
    def __init__(self, brand):
        self