# Starting money value
default money = 1000
# Rashim variable
define n = Character("Rashim")

screen display_money():
    frame:
        xpadding 15
        ypadding 15
        xalign 0.0
        yalign 0.0

        vbox:
            text "Your money: [money]$"

# The game starts here.
label start:

    scene bg outcasino # Show a background.
    "Welcome to the Grand Casino. Would you like to enter?" # Welcome dialog
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
    show screen display_money
    scene bg incasino
    with Dissolve(.5)
    show rashim neutral
    n "What game would you like to play?"
    menu:
        "Roulette":
            jump roulette
        "One Hand Bandit":
            jump slots
        "Quit Grand Casino":
            jump enter_no


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~roulette~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

label roulette:
    show screen display_money #refresh money
    hide rashim neutral # rashim hide
    scene bg roulette

    if money <= 0:
        jump casino_kick

    python:
        money_bet = renpy.input("How much do you want to bet?")

    if money_bet.isdigit():
        $ money_bet = int(money_bet)
        $ money = money - money_bet
    else:
        "Chose correct number."
        jump roulette

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
            python:
                money = money + int(money_bet)
                money_bet = 0
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
            jump roulette_win_green
        else:
            jump roulette_lose
    else:
        "Winner color is red!"
        if roulette_color == 2:
            jump roulette_win
        else:
            jump roulette_lose

label roulette_win:
    python:
            money = money + (int(money_bet)*2)
            money_bet = 0
    show screen display_money #refresh money
    "You win! Congratulation."
    jump roulette
label roulette_win_green:
    python:
            money = money + (int(money_bet)*14)
            money_bet = 0
    show screen display_money #refresh money
    "You hit jackpot green! Congratulation."
    jump roulette


label roulette_lose:
    "You lose! Good luck next time."
    jump roulette
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~roulette-end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~bandit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label slots:
    python:
        row1 = ['1_seven']

    show screen display_money #refresh money
    hide rashim neutral # rashim hide
    scene bg slots
    show 1_seven:
        yalign 0.41
        xalign 0.402
    show 2_seven:
        yalign 0.41
        xalign 0.465
    show 3_seven:
        yalign 0.41
        xalign 0.523


    if money <= 0:
        jump casino_kick

    python:
        money_bet = renpy.input("How much do you want to bet?")

    if money_bet.isdigit():
        $ money_bet = int(money_bet)
        $ money = money - money_bet
    else:
        "Chose correct number."
        jump slots




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END SCRIPTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label casino_kick:
    show screen display_money
    scene bg incasino
    with Dissolve(.5)
    show rashim neutral
    n "You lost all money get out!"
    return
label enter_no:
    # This ends the game.
    return
label under_18:
    n "Sorry people under 18 years old can't enter our Grand Casino"
    return
