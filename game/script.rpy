# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Rashim")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outcasino

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.


    "Welcome to the Grand Casino"
    "Would you like to enter?"
    menu:

        "Yes, I do.":
            jump enter_yes

        "No, i don't":
            jump enter_no

label enter_yes:
    scene bg incasino
    with Dissolve(.5)

    show rashim neutral
    n "Are you above 18 years old?"
menu:
    "Yes, I am.":
        jump above_18

    "No, I am not.":
        jump under_18
label above_18:
    n "What game would you like to play?"
menu:
    "Roulette":
        jump enter_no
    "Poker":
        jump enter_no
    "One Hand Bandit":
        jump enter_no


label under_18:
    n "Sorry people under 18 years old can't enter our Grand Casino"
label enter_no:
    # This ends the game.
    return
