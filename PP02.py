num = int(input("Pick a number:"))
check = int(input("Pick a second number:"))

if (num % 2 == 0):
    print("The number you've chosen is even")
else:
    print("The number you've chosen in odd")

if (num % 4 ==0):
    print("The number you've chose is divisible by 4")
else:
    print("The number you've choses is not divisible by 4")

if (num % check ==0):
    print("The first number you've chose is divisible by the 2nd number you've chosen")
else:
    print("The first number you've chose is not divisible by the 2nd number you've chosen")

