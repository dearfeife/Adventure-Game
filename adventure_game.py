import time
import random

monsters = ("Troll", "Gorgon", "Wicked fairie", "pirate")
monster = random.choice(monsters)


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a dark dungeon."
                "In front of you are two passageways.")
    print_pause("Rumor has it that a" + monster +
                "is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.\n")


def house(weapons):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a" +
                " " + monster + ".\n"
                "Eep! This is the" + " " + monster + "'s house!")
    print_pause("The" + monster + " attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    choice_fight = input("Would you like to (1) fight or (2) run away?\n")

    if choice_fight == '1':
        if "sword" in weapons:
            print_pause("As the gorgon moves to attack,"
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand as"
                        "you brace yourself for the attack.")
            print_pause("But the gorgon takes one look at your shiny new toy "
                        "and runs away!")
            print_pause("You have rid the town of the gorgon."
                        " You are victorious!")
            restart_game()
        else:
            print_pause("You do your best...\n"
                        "but your dagger is no match for the troll.\n"
                        "You have been defeated!")
            restart_game()

    if choice_fight == '2':
        print_pause("You run back into the field."
                    "Luckily, you don't seem to have been followed.")
        field(weapons)
    else:
        print("(Please enter 1 or 2.)")


def cave(weapons):
    print_pause("You peer cautiously into the cave.")
    if "sword" in weapons:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        field(weapons)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        weapons.append("sword")
        field(weapons)


def field(weapons):
    choice = input("Enter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "What would you like to do?\n"
                   "(Please enter 1 or 2.)\n")
    if choice == '1':
        house(weapons)
    elif choice == '2':
        cave(weapons)
    else:
        print("(Please enter 1 or 2.)")


def restart_game():
    choice_restart = input("Would you like to play again? (y/n)\n")
    if choice_restart == 'y':
        print_pause("Excellent!Restarting the game...")
        play_game()
    else:
        print_pause("Thanks for playing!See you next time.")


def play_game():
    weapons = []
    intro()
    field(weapons)


play_game()
