# Inheritance

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return "Name: {}\nAge: {}\nHeight: {}".format(self.name, self.age, self.height)
    def get_older(self, years):
        self.age += years

class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
    def __str__(self):
        text = super(Worker, self).__str__()
        text += "\nSalary: {}".format(self.salary)
        return text
    def calc_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Henry", 40, 174, 3000)
print(worker1)
print("Yearly Salary: {}".format(worker1.calc_yearly_salary()))