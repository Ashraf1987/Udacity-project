import time
import random


### variables and randommes
melee_weapon = random.choice(
    ["Spirit sword", "Holy dagger", "Demonic chainsaw", "Demonic long sword"]
)
monster = random.choice(
    ["Ghost", "Skelleton", " Zompie", "half demon", "impure vampire"]
)
color = random.choice(["Blue", "Black", "Red", "white", "purple"])
ranged_weapons = random.choice(
    [
        " Holy arrows ",
        " Fire cross bow ",
        " ultrasonic waves ",
        " Demonic shot guns",
    ]
)
current_points = 30

def End():
     print_pause("Thanks for playing! Goodbye.")
     print_pause("If you want to play again after some time enter yes")
### Asks if player wants to play again
def play_over():
     while True:
        choice = input("Would you like to play again? (yes/no): ").lower()
        if choice == 'yes':
            game_intro()
            break
        elif choice == 'no':
          End()
        else:
          print("Invalid input. Please enter 'yes' or 'no'.")


### function to  to tell you how good you are in the game
def points(current_points):
    if current_points == 60:
        print_pause("You clear the game")
        print_pause("Oh my you are so good at this game")
        play_over()
    elif 0 < current_points < 50:
        print_pause("You clear the game")
        print_pause("You are gaming skills are pretty average ")
        play_over()


### Time.sleep function
def print_pause(string: str):
    print(string)
    print("")
    time.sleep(1)


### game intro
def game_intro():
    print_pause("current point =")
    print_pause(current_points)
    print_pause("Welcome to the ancient house")
    print_pause("You are a Spirit hunter and you have been")
    print_pause("tasked to purify A house of Its Dark spirits")
    ### loop to handle invalid input
    while True:
        intro = input("(Please enter 1 to enter first room)")
        if intro == "1":
            first_room(melee_weapon, color, monster, current_points)
            break
        else:
            intro = input("(Please enter 1 to enter first room)")


### first room function
def first_room(melee_weapon, color, monster, current_points):
    print_pause("You enter the first room")
    print_pause("You see a very terrifying " + color + monster)
    print_pause("Enter 1 To use your melee weapon to kill it")
    print_pause("Enter 2 To use escape")
    ### loop to handle invalid input
    while True:
        First_Room = input("(Please enter 1 or 2:")
        if First_Room == "1":
            print_pause("You tear the monster to shreds using" + melee_weapon)
            print_pause("You clear the first room")
            ### Increasing total points
            current_points = current_points + 10
            print_pause("current_points =")
            print_pause(current_points)
            second_room1 = input("(Please enter 1 to enter second room)")
            if current_points == 0:
               print_pause("game over")
               print_pause("You suck at this game")
               play_over()
               break
            while True:
               if second_room1 == "1":
                    second_room(
                    melee_weapon,ranged_weapons, color,monster,current_points
                    )
                    break
               else:
                    second_room1 = input("(Enter 1 to enter second room )")
        elif First_Room == "2":
            print_pause("You manage to escape but you were injured")
            ### decreasing total points
            current_points = current_points - 10
            print_pause("current_points =")
            print_pause(current_points)
            ### losing condition
            if current_points == 0:
               print_pause("game over")
               print_pause("You suck at this game")
               play_over()
               break
            ###Entering The first room again
            while True:
                intro = input("(Please enter 1 to enter first room)")
                if intro == "1":
                    first_room(
                    melee_weapon,color,monster,current_points
                    )
                    break
                else:
                    intro = input("(Please enter 1 to enter first room)")
### Secound room function
def second_room(melee_weapon, ranged_weapons, color, monster, current_points):
    print_pause("You Enter The second room")
    ### conditional loop to handle invalid input
    print_pause("You see a" + color + monster + "at a distance")
    while True:
        Second_Room = input("(enter 1to use meleeweapon or 2 to use rangedweapon:")
        if Second_Room == "1":
            print_pause(
               "You run at the monster to kill him using a " + melee_weapon
            )
            print_pause("But the" + monster + "spits poison on you")
            ### decrasing total points
            current_points = current_points - 10
            print_pause("current_points=")
            print_pause(current_points)
            ### losing condition
            if current_points == 0:
               print_pause("game over")
               print_pause("You suck at this game")
               play_over()
               break
            while True:
                second_room2 = input("(Enter 1 to enter second room)")
                if second_room2 == "1":
                    second_room(
                    melee_weapon,ranged_weapons,color,monster,current_points
                    )
                    break
                else:
                    second_room2 = input("(Enter 1 to enter second room)")
                    break
        elif Second_Room == "2":
            print_pause("You use your" + ranged_weapons + "To kill it")
            ### incrasing total points
            current_points == current_points + 10
            print_pause("You clear the second room ")
            current_points = current_points + 10
            print_pause("current_points=")
            print_pause(current_points)
            print_pause("You have unloucked ultimate attacks")
            while True:
                boss_room1 = input("(Please enter 1 to enter boss room)")
                if boss_room1 == "1":
                    boss_room(ranged_weapons, color, current_points)
                    break
                else:
                    boss_room1 = input("(Please enter 1 to enter boss room )")
     

### boss room function
def boss_room(ranged_weapons, color, current_points):
    print_pause("You Enter The third room")
    print_pause("You see a massive" + color + "Demon")
    while True:
        ### conditional loop to handle invalid input
        Input = input(
            "(Enter 1 to use ultimate attack or 2 to use ranged weapon:"
        )
        if Input == "1":
            print_pause("A black hole swallows the Demon ")
            print_pause("current points =")
            ### decrasing total points
            current_points = current_points + 10
            print_pause(current_points)
            points(current_points)
            play_over()
            break
        elif Input == "2":
            print_pause("You use your"+ ranged_weapons + "does not damage it")
            print_pause(
               "the demon throws his weapon on you"
            )
            ### decrasing total points
            print_pause("current points =")
            current_points = current_points - 10
            print_pause(current_points)
            ### losing condition
            if current_points == 0:
               print_pause("game over")
               print_pause("You suck at this game")
               play_over()
               break
            while True:
                boss_room2 = input("(Please enter 1 to enter boss room)")
                if boss_room2 == "1":
                    boss_room(ranged_weapons, color, current_points)
                else:
                    boss_room2 = input("(Please enter 1 to enter boss room)")
                    break
            print_pause(current_points)
            break



game_intro()