# Starting money value
default money = 1000
# Rashim variable
define n = Character("Rashim")
# slots image list
default slots_icons = ["seven.png","bar.png", "banana.png"]

init python:
    import random

screen display_money(): # money ui
    frame:
        xpadding 15
        ypadding 15
        xalign 0.0
        yalign 0.0

        vbox:
            text "Your money: [money]$"

label spin:
    if persistent.counter < 10:
        $ random_image_row1_indicator = renpy.random.randint(0, len(slots_icons)-1)
        $ random_image_row2_indicator = renpy.random.randint(0, len(slots_icons)-1)
        $ random_image_row3_indicator = renpy.random.randint(0, len(slots_icons)-1)

        $ random_image_row1 = slots_icons[random_image_row1_indicator]
        $ random_image_row2 = slots_icons[random_image_row2_indicator]
        $ random_image_row3 = slots_icons[random_image_row3_indicator]

        show expression Image("images/slots/" + random_image_row1):
            yalign 0.41
            xalign 0.402
        show expression Image("images/slots/" + random_image_row2):
            yalign 0.41
            xalign 0.465
        show expression Image("images/slots/" + random_image_row3):
            yalign 0.41
            xalign 0.523
        pause(0.15) # pause between images

        $ persistent.counter += 1

        jump spin
    else:
        if random_image_row1 == random_image_row2 == random_image_row3:
            "Congratulation you win!"
            if random_image_row1_indicator == 0:
                $ money = money + (int(money_bet)*100)
                $ money_bet = 0
            elif random_image_row1_indicator == 1:
                $ money = money + (int(money_bet)*10)
                $ money_bet = 0
            elif random_image_row1_indicator == 2:
                $ money = money + (int(money_bet)*5)
                $ money_bet = 0
        else:
            "Yuo lost. Good luck next time."

        # Reseting counter
        $ persistent.counter = 0

        return



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
    show screen display_money #refresh money
    hide rashim neutral # rashim hide
    scene bg slots
    show slots_rewards:
        xalign 1.0
        yalign 0.0

label slots_next:
    show screen display_money #refresh money
    if money <= 0:
        jump casino_kick

    menu:
        "Spin":
            jump slots_next_2
        "Go Back":
            jump game_choice

label slots_next_2:

    python:
        money_bet = renpy.input("How much do you want to bet?")
    if money_bet.isdigit():
        $ money_bet = int(money_bet)
        $ money = money - money_bet
    else:
        "Chose correct number."
        jump slots

    $ persistent.counter = 0
    call spin
    jump slots_next



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
