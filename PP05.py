from random import seed
from random import randint
seed(randint)

a = []
for _ in range(15):
	value = randint(0, 25)
	a.append(value)

b = []
for _ in range(10):
    value = randint(0, 25)
    b.append(value)
print(a)
print(b)

c = []
if b >= a:
    for value in (b):
        if value in a:
            c.append(value)
else:    
    for value in (a):
        if value in b:
            c.append(value)

print(c)