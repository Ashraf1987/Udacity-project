import time
import random

# Variables and random choices
melee_weapon = random.choice(
    ["Spirit sword", "Holy dagger", "Demonic chainsaw", "Demonic long sword"]
)
monster = random.choice(
    ["Ghost", "Skeleton", "Zombie", "Half demon", "Impure vampire"]
)
color = random.choice(["Blue", "Black", "Red", "White", "Purple"])
ranged_weapons = random.choice(
    ["Holy arrows", "Fire crossbow", "Ultrasonic waves", "Demonic shotguns"]
)
current_points = 30


def end_game():
    print_pause("Thanks for playing! Goodbye.")
    print_pause("If you want to play again after some time, enter 'yes'.")
    exit()


def game_over():
    while True:
        choice = input("Would you like to play again? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            game_intro()
            break
        elif choice in ["no", "n"]:
            end_game()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def update_points(current_points):
    if current_points == 60:
        print_pause("You cleared the game!")
        print_pause("Oh my, you are so good at this game.")
        game_over()
    elif 0 < current_points < 50:
        print_pause("You cleared the game!")
        print_pause("Your gaming skills are pretty average.")
        game_over()


def print_pause(message: str):
    print(message)
    print("")
    time.sleep(1)


def game_intro():
    print_pause("Welcome to the ancient house.")
    print_pause("You are a Spirit hunter and you have been")
    print_pause("tasked with purifying a house of its dark spirits.")
    
    while True:
        player_action = input("Enter 1 to enter the first room and 2 to leave: ")
        if player_action == "1":
            first_room(current_points)
            break
        elif player_action == "2":
            print_pause("You leave.")
            exit()


def first_room(current_points):
    print_pause("You enter the first room.")
    print_pause(f"You see a very terrifying {color} {monster}.")
    print_pause("Enter 1 to use your melee weapon.")
    print_pause("Enter 2 to use escape.")
    
    while True:
        if current_points == 0:
            print_pause("Game over.")
            print_pause("You suck at this game.")
            game_over()
        
        player_action = input("Please enter (1/2): ")
        if player_action == "1":
            print_pause(f"You tear the monster to shreds using {melee_weapon}.")
            print_pause("You clear the first room!")
            current_points += 10
            print_pause(f"Current points: {current_points}")
            player_action = input("Enter 1 to enter the second room or 2 to leave: ")
            while True:
                if player_action == "1":
                    second_room(current_points)
                elif player_action == "2":
                    print_pause("You leave.")
                    exit()
        
        elif player_action == "2":
            print_pause("You manage to escape, but you were injured.")
            current_points -= 10
            print_pause(f"Current points: {current_points}")
            
            while True:
                player_action = input("Enter 1 to enter the first room and 2 to leave: ")
                if player_action == "1":
                    first_room(current_points)
                    break
                elif player_action == "2":
                    print_pause("You leave.")
                    exit()


def second_room(current_points):
    print_pause("You enter the second room.")
    print_pause(f"You see a {color} {monster} in the distance.")
    
    while True:
        if current_points == 0:
            print_pause("Game over.")
            print_pause("You suck at this game.")
            game_over()
        
        print_pause("Enter 1 to use melee weapon.")
        print_pause("Enter 2 to use ranged weapon.")
        player_action = input("Enter (1/2): ")
        
        if player_action == "1":
            print_pause(f"You run at the monster to kill it using a {melee_weapon}.")
            print_pause("But the monster spits poison on you.")
            current_points -= 10
            print_pause(f"Current points: {current_points}")
            while True:
                player_action = input("Enter 1 to enter the second room: ")
                if player_action == "1":
                    second_room(current_points)
                else:
                    player_action = input("Enter 1 to enter the second room: ")
                    break
        
        elif player_action == "2":
            print_pause(f"You use your {ranged_weapons} to kill it.")
            current_points += 10
            print_pause("You clear the second room!")
            print_pause(f"Current points: {current_points}")
            print_pause("You have unlocked ultimate attacks.")
            
            while True:
                player_action = input("Enter 1 to enter the boss room or 2 to leave: ")
                if player_action == "1":
                    boss_room(current_points)
                elif player_action == "2":
                    print_pause("You leave.")
                    exit()


def boss_room(current_points):
    print_pause("You enter the third room.")
    print_pause(f"You see a massive {color} demon.")
    
    while True:
        if current_points == 0:
            print_pause("Game over.")
            print_pause("You suck at this game.")
            game_over()
        
        print_pause("Enter 1 for ultimate attack.")
        print_pause("Enter 2 for ranged attack.")
        player_action = input("Enter (1/2): ")
        
        if player_action == "1":
            print_pause("A black hole swallows the demon.")
            current_points += 10
            print_pause(f"Current points: {current_points}")
            update_points(current_points)
            game_over()
            break
        
        elif player_action == "2":
            print_pause(f"You use your {ranged_weapons}, but it does not damage it.")
            print_pause("The demon throws his weapon at you.")
            current_points -= 10
            print_pause(f"Current points: {current_points}")
            
            while True:
                player_action = input("Please enter 1 to enter the boss room or 2 to leave: ")
                if player_action == "1":
                    boss_room(current_points)
                elif player_action == "2":
                    print_pause("You leave.")
                    exit()


game_intro()
