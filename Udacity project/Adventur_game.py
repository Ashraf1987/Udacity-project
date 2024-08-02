import time
import random


# Define global variables
MELEE_WEAPONS = ["Spirit sword", "Holy dagger", "Demonic chainsaw", "Demonic long sword"]
MONSTERS = ["Ghost", "Skeleton", "Zombie", "Half demon", "Impure vampire"]
COLORS = ["Blue", "Black", "Red", "White", "Purple"]
RANGED_WEAPONS = ["Holy arrows", "Fire crossbow", "Ultrasonic waves", "Demonic shotguns"]
INITIAL_POINTS = 30


def print_pause(message: str) -> None:
    """Prints a message with a pause."""
    print(message)
    time.sleep(1)


def end_game() -> None:
    """Ends the game and prompts to play again."""
    print_pause("Thanks for playing! Goodbye.")
    play_again = input("If you want to play again, enter 'yes': ").lower()
    if play_again == "yes":
        game_intro()
    else:
        print_pause("Goodbye!")


def adjust_points(points: int, amount: int) -> int:
    """Adjusts the current points and checks if the game is over."""
    points += amount
    if points <= 0:
        print_pause("Game over. You suck at this game.")
        end_game()
    return points


def game_intro() -> None:
    """Introduces the game and starts the first room."""
    melee_weapon = random.choice(MELEE_WEAPONS)
    monster = random.choice(MONSTERS)
    color = random.choice(COLORS)
    ranged_weapon = random.choice(RANGED_WEAPONS)
    current_points = INITIAL_POINTS

    print_pause(f"Current points: {current_points}")
    print_pause("Welcome to the ancient house.")
    print_pause("You are a Spirit hunter tasked with purifying a house of its dark spirits.")

    while True:
        choice = input("Enter '1' to enter the first room: ")
        if choice == "1":
            first_room(melee_weapon, color, monster, ranged_weapon, current_points)
            break


def first_room(melee_weapon: str, color: str, monster: str, ranged_weapon: str, current_points: int) -> None:
    """Handles the first room of the game."""
    print_pause(f"You enter the first room and see a terrifying {color} {monster}.")
    print_pause("Enter '1' to use your melee weapon to kill it or '2' to escape.")

    while True:
        choice = input("Choose an option (1 or 2): ")
        if choice == "1":
            print_pause(f"You tear the {monster} to shreds using {melee_weapon}.")
            current_points += 10
            print_pause(f"Current points: {current_points}")

            while True:
                next_room = input("Enter '1' to enter the second room: ")
                if next_room == "1":
                    second_room(melee_weapon, ranged_weapon, color, monster, current_points)
                    break
        elif choice == "2":
            print_pause("You manage to escape but you were injured.")
            current_points = adjust_points(current_points, -10)
            print_pause(f"Current points: {current_points}")
        else:
            print_pause("Invalid input. Please enter '1' or '2'.")


def second_room(melee_weapon: str, ranged_weapon: str, color: str, monster: str, current_points: int) -> None:
    """Handles the second room of the game."""
    print_pause(f"You enter the second room and see a {color} {monster} at a distance.")
    print_pause("Enter '1' to use melee weapon or '2' to use ranged weapon.")

    while True:
        choice = input("Choose an option (1 or 2): ")
        if choice == "1":
            print_pause(f"You run at the {monster} with your {melee_weapon}.")
            print_pause(f"But the {monster} spits poison on you.")
            current_points = adjust_points(current_points, -10)
        elif choice == "2":
            print_pause(f"You use your {ranged_weapon} to kill the {monster}.")
            current_points += 20
            print_pause(f"Current points: {current_points}")
            print_pause("You have unlocked ultimate attacks.")

            while True:
                next_room = input("Enter '1' to enter the boss room: ")
                if next_room == "1":
                    boss_room(ranged_weapon, color, current_points)
                    break
        else:
            print_pause("Invalid input. Please enter '1' or '2'.")


def boss_room(ranged_weapon: str, color: str, current_points: int) -> None:
    """Handles the boss room of the game."""
    print_pause(f"You enter the boss room and see a massive {color} demon.")
    print_pause("Enter '1' to use ultimate attack or '2' to use ranged weapon.")

    while True:
        choice = input("Choose an option (1 or 2): ")
        if choice == "1":
            print_pause("A black hole swallows the demon.")
            current_points += 10
            print_pause(f"Current points: {current_points}")
            if current_points >= 60:
                print_pause("You cleared the game! You are so good at this game!")
            else:
                print_pause("You cleared the game. Your gaming skills are pretty average.")
            end_game()
            break
        elif choice == "2":
            print_pause(f"You use your {ranged_weapon}, but it does not damage the demon.")
            print_pause("The demon throws his weapon at you.")
            current_points = adjust_points(current_points, -10)
        else:
            print_pause("Invalid input. Please enter '1' or '2'.")


# Start the game
game_intro()
