from random import seed
from random import randint
seed(randint)

x = 1
n = int(0)
while (x == 1):
    
    a = randint(1,9)
    b = int(input("Pick a number between 1 and 9"))

    if (b > a):
        print("Too high!")
        again = input("play again (Y or N)")
        n = (n + 1)
    if (b < a):
        print("Too low!")
        again = input("play again (Y or N)")
        n = (n + 1)
    if (b == a):
        print("You got it!")
        again = input("play again (Y or N)")
        n = (n + 1)
    if (again == "n" or again == "N"):
        x = 2
        print(f"You played {n} times")
