Name = input("What's your name? ")
print("Your name is " + Name)

Age = int(input("How old are you? "))
print(f"You are {Age} years old")

till100 = (100 - Age)
from datetime import date
today = date.today()
year = int(today.strftime("%Y"))
year100 = (year) + (till100)


print(f"{Name}, you will turn 100 in the year {year100}")


