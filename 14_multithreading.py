import threading

# def helloworld():
#     print("Hello World!")

# t1 = threading.Thread(target=helloworld)
# t1.start()

def func1():
    for x in range(100):
        print("Function 1")
def func2():
    for y in range(100):
        print("Function 2")

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()