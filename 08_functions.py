# Functions

# def helloworld():
#     print("Helloo Python!!")
  
# helloworld()

# def add(x, y):
#     print(x + y)

# add(6,9)

def mysum(*numbers): # Multiple items > numbers (keyword = *)
    result = 0
    for number in numbers:
        result += number
    return result;
print(mysum(10,20,30,40,50))