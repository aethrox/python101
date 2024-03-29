# Events and Daemon Threads
import threading
import time

# event = threading.Event()

# def myfunction():
#     print("Waiting for event to trigger...")
#     event.wait()
#     print("Performing action XYZ now...")

# t1 = threading.Thread(target=myfunction)
# t1.start()

# x = input("Do you want to trigger the event? (y/n)")
# if x == "y":
#     event.set()

path = "file.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(10):
        print(text)
        time.sleep(2)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
