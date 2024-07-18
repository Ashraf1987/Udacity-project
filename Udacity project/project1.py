import time
import random
import func


### Prints the entered string with a pause
def print_pause(string:str):
    print(string)
    print("")
    time.sleep(1)
### Game welcome screen
func.print_pause("Welcome to the ancient house")
func.print_pause("You are a Spirit hunter and you have been asked to purify A house of Its Dark spirits")
### First room  
Weapon = random.choice(["Weak Spirit sword","Holy dagger","weak ultrasonic waves"])
Monster = random.choice(["Ghost"," Skelleton"])
Color = random.choice(["Blue","Black","Red"])
Health = 100

func.print_pause("You Enter The First Room")
func.print_pause("There You See A very")
func.print_pause("You see a terrifying " + Color + Monster)
func.print_pause("Enter 1 To use your " + Weapon +" to kill it")
func.print_pause("Enter 2 To use escape")
roomChoice = input("Input: ")
if (roomChoice == "1"):
    func.print_pause("You Successfully Clear the First Room") 
elif (roomChoice == "2"):
 Health = 100 - 3
 func.print_pause("THE Undead Takes 30 from your Health" ) 

