# If Else Statements

x = input("First number: ")
y = input("Second number: ")

x = int(x)
y = int(y)

if x < y:
    print("x is less than y!")
    if x > 0:
        print("x is a positive number.")
    elif x == 0:
        print("x is a neutral number.")
    else:
        print("x is a negative number.")
elif x > y:
    print("x is greater than y!")
else:
    print("x is equal to y!")