#for reference, "Yo banana boy" is a palindrome
    
string = input("Write us a word:")
count = (len(string))
print(count)

s = string[0:]
print(s)

r = string[::-1]
print(r)

if s == r:
    print("that word is a palindrome")
else:
    print("that word is not a palindrome")
