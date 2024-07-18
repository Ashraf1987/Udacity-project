import time
import random
import func
 

func.print_pause("welcome")
func.print_pause("Type 1 for game details")
func.print_pause("Type 2 To get straight to the introduction")
### Prompt user for a choice 
while True:
    roomChoice = input("Input: ")
    if (roomChoice == "1"):
        func.print_pause("The Game consists of Two Floors Each Floors conists of 3rooms and a boss room ") 
        func.print_pause("You are a Spirit hunter and you have been asked to purify A house of Its Dark spirits")
        func.print_pause("Type 1 To show Player Status")
        func.print_pause("Type 2 To enter the first room")
        roomChoice = input("Room Choice: ")
        if (roomChoice == "1"):
            func.print_pause("Healt = 50")
            func.print_pause("Attack damage = 30")
        elif (roomChoice == "2"):
            func.print_pause("You enter The first room")
        while roomChoice != "1" and roomChoice != "2":
            print ('Enter a valid input')
            break
    elif (roomChoice == "2"):
        print("You are a Spirit hunter and you have been asked to purify A house of Its Dark spirits")
        break
    while roomChoice != "1" and roomChoice != "2":
        print ('Enter a valid input')
        break
        