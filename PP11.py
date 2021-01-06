num = int(input("Pick a number:"))

x = range(1, (num+1))
divs = []
for elem in x:
    if (num % elem == 0):
        divs.append(elem)
        
prime = [1, num]
if (divs == prime):
    print("That's a prime number!")
else:
    print("That's not a prim number :( ")


