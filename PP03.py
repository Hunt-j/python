a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = []
for element in a:
    if element < 5:
        x.append(element)
print(x)

num = int(input("Pick a number:"))
y = []
for element in a:
    if element < num:
        y.append(element)
print(y)