# Classes and Objects

# class Person:
    
#     def __init__(self):
#         print("Hello World!")

# x = Person()

class Person: 
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __del__(self):
        print("Object deleted!")
    
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(person1.name, person1.age, person1.height)

    def helloworld(self):
        print("Hello World!")

person1 = Person("John", 19, 190)

person1.helloworld()

print(person1)

del person1