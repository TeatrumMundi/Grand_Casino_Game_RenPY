define n = Character("Rashim")
# The game starts here.
label start:
    # Show a background.
    scene bg outcasino

    #Welcome dialog
    "Welcome to the Grand Casino. Would you like to enter?"
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
            jump roulette
        "Poker":
            jump enter_no
        "One Hand Bandit":
            jump enter_no

label roulette:
    hide rashim neutral
    scene bg roulette
    with Dissolve(0.5)
    n "Choose color you want to bet on"
    menu:
        "Black":
            jump enter_no

label enter_no:
    # This ends the game.
    return
label under_18:
    n "Sorry people under 18 years old can't enter our Grand Casino"
    return
