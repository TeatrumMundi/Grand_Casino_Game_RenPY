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
    scene bg 18
    with Dissolve(.5)
    "Are you above 18 years old?"
    menu:
        "Yes, I am.":
            jump game_choice
        "No, I am not.":
            jump under_18

label game_choice:
    scene bg incasino
    with Dissolve(.5)
    show rashim neutral
    n "What game would you like to play?"
    menu:
        "Roulette":
            jump roulette
        "Poker":
            jump enter_no
        "One Hand Bandit":
            jump enter_no
        "Quit Grand Casino":
            jump enter_no

label roulette:
    hide rashim neutral
    scene bg roulette
    with Dissolve(0.5)
    n "Choose color you want to bet on."
    menu:
        "Black":
            jump black
        "Red":
            jump red
        "Green":
            jump green
        "Go Back":
            jump game_choice
label black:
    $ roulette_color = 1
    jump roulette_spin
label red:
    $ roulette_color = 2
    jump roulette_spin
label green:
    $ roulette_color = 3
    jump roulette_spin

label roulette_spin:
    if roulette_color == 1:
        "You chose black."
    elif roulette_color == 2:
        "You chose red."
    else:
        "You chose green."

    $ random_numer = renpy.random.randint(1, 37)
    if random_numer <= 18:
        "Winner color is black!"
        if roulette_color == 1:
            jump roulette_win
        else:
            jump roulette_lose
    elif random_numer == 37:
        "Winner color is green!"
        if roulette_color == 3:
            jump roulette_win
        else:
            jump roulette_lose
    else:
        "Winner color is red!"
        if roulette_color == 2:
            jump roulette_win
        else:
            jump roulette_lose

label roulette_win:
    "You win! Congratulation."
    jump roulette

label roulette_lose:
    "You lose! Good luck next time."
    jump roulette

label enter_no:
    # This ends the game.
    return
label under_18:
    n "Sorry people under 18 years old can't enter our Grand Casino"
    return
