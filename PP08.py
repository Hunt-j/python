

def roshambo(choice):
    if choice == "R" or choice == "r":
        return 2 
    elif choice == "P" or choice == "p":
        return 3
    elif choice == "S" or choice == "s":
        return 4
    else:
        print("Didn't pick a correct option")
    

x = 1

while (x == 1):
    a = input("Rock (R), paper (P), or scissors (S)?")
    b = input("Rock (R), paper (P), or scissors (S)?")

    p1 = roshambo(a)
    p2 = roshambo(b)

    win = (p1**p2)

    if ((win == 4) or (win == 27) or (win == 256)):
            print("It's a tie!")
            again = input("Play again (Y or N)?")
    else:

        if (p1 == 2):
            if (win == 16):
                print("Congratulations player 1, you've won!")
                again = input("play again (Y or N)")
            else:
                print("Congratulations player 2, you've won!")
                again = input("play again (Y or N)")

        if (p1 == 3):
            if ((win == 9) or (win == 8)): 
                print("Congratulations player 1, you've won!")
                again = input("play again (Y or N)")
            else:
                print("Congratulations player 2, you've won!")
                again = input("play again (Y or N)")

        if (p1 == 4):
            if ((win == 64) or (win == 81)):
                print("Congratulations player 1, you've won!")
                again = input("play again (Y or N)")
            else:
                print("Congratulations player 2, you've won!")
                again = input("play again (Y or N)")
    
    if (again == "N" or again == "n"):
        x = 2

        
        
    

