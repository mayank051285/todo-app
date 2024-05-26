import random
x = int(input("Enter the lower bound: "))
y = int(input("Enter the upper bound: "))

if x > y:
    print("Wrong input, Try again")
else:
    print(random.randint(x, y))
