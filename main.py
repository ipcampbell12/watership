""" Gameplay happens through this file """

# modules
import text
import rabbits
import events
import random

# Global variables
char = None
game_progress = 0

# funcs


def change_progress(change):
    global game_progress
    game_progress += change
    if change == 0:
        my_text = (f"Your game progress remains unchanged at{game_progress} ")
        x = my_text.center(20)
        print(x)
    elif change > 0:
        my_text = (f"Your game progress has increased to {game_progress}")
        x = my_text.center(20)
        print(x)
    elif change < 0:
        my_text = (f"Your game progress has decreased to {game_progress}")
        x = my_text.center(20)
        print(x)


def sum_points(character):
    total = character.hp + character.strength + character.courage + character.influence + \
        character.kindness + character.strength + \
        character.cleverness + character.charisma
    print(f"Your final score is {total} points!")


# Part 1: Choose your rabbit
print(text.welcome)
print(text.rabbits)
print(text.rab1)
print(text.rab2)
print(text.rab3)

while True:
    while True:
        rab = input("Please enter the name of a rabbit: ")
        for rabbit in rabbits.all_rabbits:
            if rab == rabbit.name:
                rabbit.show_stats()
                rab_select = input(
                    f"Would you like to choose {rabbit.name} as your rabbit? (Yes/No)")
                if rab_select == "Yes":
                    char = rabbit
                    print(f"""
                    You have selected {char.name} as your rabbit.
                    Your starting health is {char.hp} health points
                    Your starting influence is {char.influence} influence points
                    """)
                    break
                elif rab_select == "No":
                    continue
                elif rab_select != "Yes" or rab_select != "No":
                    print("Invalid input. Please enter a Yes or a No")
        else:
            print("Invalid input.Please select a valid rabbit")
            continue
        break

    # Part 2: Leave the warren
    h1 = text.heading1
    h1a = h1.center(24)
    print(h1a)

    print(text.danger)
    print(text.dog)
    print(text.options)
    while True:
        event1_choice = input(
            """
            1. run through woods
            2. float accross stream. Please enter a number:""")
        if event1_choice == "1":
            if char.strength - events.event1_op1.fatigue < 0:
                print(text.tired)
                print(text.perished)
                print(text.game_over)
                # Need to figure out this part
                break
            else:
                print(text.tired2)
                char.change_hp(events.event1_op1.energy)
                char.change_influence(events.event1_op1.influence)
                char.change_cleverness(-1)
                change_progress(2)
                break
        if event1_choice == "2":
            print(text.stream)
            char.change_hp(events.event1_op2.energy)
            char.change_influence(events.event1_op2.influence)
            char.change_cleverness(2)
            change_progress(2)
            break
    while True:
        cont = input("Continue playing? Y/N")
        if cont.lower() == "y":
            break
        else:
            print(text.ended)
            exit()

    print(text.wandering)
    print(text.day_or_so)

    while True:
        cont = input("Continue playing? Y/N")
        if cont.lower() == "y":
            break
        else:
            print(text.ended)
            exit()

    while True:
        val = random.choice(list(events.more_possibilities.items()))
        x, y = val
        print(y)
        if x == 1:
            char.change_hp(30)
            char.change_strength(1)
            break
        elif x == 2:
            char.change_hp(-20)
            char.change_strength(-1)
            break
        elif x == 3:
            char.change_hp(-20)
            break
        elif x == 4:
            char.change_strength(2)
            char.change_courage(3)
            char.change_influence(15)
            char.change_hp(-10)
            break
        elif x == 5:
            char.change_hp(-15)
            char.change_strength(-1)
            break

    while True:
        cont = input("Continue playing? Y/N")
        if cont.lower() == "y":
            break
        else:
            print(text.ended)
            exit()

# Part 3: Cowslip
    h2 = text.heading2
    h2a = h2.center(24)
    print(h2a)

    print(text.cowslip1)
    print(text.cowslip2)

    while True:
        event2_choice = input("""
    1. You accept his offer and decide to live with the rabbits
    2. You thank him but choose to press on ahead to the large hill in the distance
    Please enter a number: """)
        if event2_choice == "1":
            print(text.hospitable)
            print(text.veggies)
            char.change_hp(events.event2_op1.energy)
            char.change_influence(events.event2_op1.influence)
            change_progress(2)
            print(text.sad)
            keep_going1 = input("Continue playing? Y/N")
            if keep_going1 == "Y":
                print(text.fiver_no_like)
                print(text.bigwig_trapped)
                print(text.sense)
                help_bw = input(
                    """
                    Do you . . .
                    1. Help Bigwig
                    2. Leave him and run away """)
                if help_bw == "1":
                    char.change_hp(-15)
                    char.change_influence(30)
                    char.change_courage(1)
                    print(
                        "Bigwig is free but injured. It's time to leave this terrible place!")
                    change_progress(2)
                    break
                else:
                    print(
                        "Without Bigwig, there's no chance of survival of the new warren. The game is over")
                    print(text.game_over)
                    exit()
            else:
                print(text.ended)
                exit()
        elif event2_choice == "2":
            print(text.upset)
            char.change_hp(events.event2_op2.energy)
            char.change_influence(events.event2_op2.influence)
            char.change_courage(2)
            change_progress(3)
            keep_going2 = input("Continue playing? Y/N")
            if keep_going2 == "Y":
                print(text.watership1)
                change_progress(1)
                char.change_hp(50)
                char.change_influence(35)
                char.change_charisma(2)
                break
            else:
                print(text.ended)
                break
    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    # Part 4 Kehaar
    h3 = text.heading3
    h3a = h3.center(24)
    print(h3a)

    print(text.kehaar1)
    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)
    print(text.kehaar2)
    while True:
        event3_choice = input("""Do you:
        1) Help the gull and nurse him back to health
        2) Leave him alone
        """)
        if event3_choice == "1":
            char.change_hp(events.event3_op1.energy)
            char.change_influence(events.event3_op1.influence)
            char.change_kindness(2)
            char.change_strength(2)
            char.change_cleverness(1)
            change_progress(1)

            break
        elif event3_choice == "2":
            char.change_hp(events.event3_op2.energy)
            char.change_influence(events.event3_op2.influence)
            char.change_kindness(-1)
            char.change_cleverness(1)
            break

    # Part 5: Efafra1
    h4 = text.heading4
    h4a = h4.center(24)
    print(h4a)

    print(text.journey1)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.persuade)

    while True:
        efafra_select = input("""
        Do you: 
        1. Make all the rabbits come with you
        2. Allow those who prefer to stay to remain at Watership
        """)
        if efafra_select == "1":
            print(text.all_come)
            char.change_strength(2)
            char.change_hp(50)
            char.change_kindness(-2)
            char.change_influence(5)
            change_progress(1)

            break
        elif efafra_select == "2":
            print(text.some_come)
            char.change_strength(-1)
            char.change_hp(10)
            char.change_kindness(3)
            char.change_influence(20)
            change_progress(1)
            break

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.rest)
    print(text.while_rest)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    while True:
        val = random.choice(list(events.possibilities.items()))
        x, y = val
        print(y)
        if x == 1:
            char.change_hp(30)
            char.change_strength(1)
            break
        elif x == 2:
            char.change_hp(-20)
            break
        elif x == 3:
            char.change_hp(-20)
            break
        elif x == 4:
            char.change_strength(-2)
            char.change_cleverness(-1)
            break
        elif x == 5:
            char.change_hp(40)
            char.change_strength(1)
            char.change_cleverness(2)
            break

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.scouts2)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.infiltrate)

    print(text.bold)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.impressesd)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.invite)

    while True:
        invite_b = input("""Do you: 
        1. Invite Blackavar to come with you.
        2. Leave him there.""")

        if invite_b == "1":
            print(text.yes_blackavar)
            char.change_kindness(2)
            char.change_strength(3)
            char.change_hp(-15)
            char.change_charisma(2)
            char.change_influence(10)
            break
        elif invite_b == "2":
            print(text.no_blackavar)
            char.change_kindness(-1)
            char.change_hp(30)
            char.change_charisma(-1)
            char.change_influence(-20)
            break

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.woundwort)

    while True:
        keep_going = input("Continue playing? Y/N")
        if keep_going == "Y":
            break
        else:
            print(text.ended)

    print(text.woundwort2)

    while True:
        fight = input("""
        Do you: 
        1. Stay and fight the general 
        2. Escape while you can and help the does to safety 
        """)
        if fight == "1" and char.strength < rabbits.woundwort.strength:
            print("""
            You are not strong enough to fight the general. You should have escaped. The game is over
            """)
            break
        if fight == "1" and char.strength >= rabbits.woundwort.strength:
            print("""You are locked in a battle with the general. You just might have a chance. Here are your options . . .""")
            while char.hp >= 0 and rabbits.woundwort.hp >= 0:
                options = input("""
             1. Give him a cuff to the head
             2. Scratch his face 
             3. Crush him with your body wegith
             4. Bite his shoulder
            """)
                if options == "1":
                    char.cuff(rabbits.woundwort)
                    rabbits.woundwort.scratch(char)
                elif options == "2":
                    char.scratch(rabbits.woundwort)
                    rabbits.woundwort.bite(char)
                elif options == "3":
                    char.crush(rabbits.woundwort)
                    rabbits.woundwort.cuff(char)
                elif options == "4":
                    char.bite(rabbits.woundwort)
                    rabbits.woundwort.crush(char)
            if char.hp <= 0:
                print(
                    f"{char.name} has been defeated, and the general has won. Watershp is doomed")
                game_progress = 0
                print(f"You game progress is now 0. The game is over and you have lost.")
                print(text.game_over)
                break
            elif char.hp >= 0:
                print(
                    f"{char.name} has defeated the general! The rabbits of watership have won and the does are free! ")
                change_progress(4)
                char.change_influence(50)
                char.change_courage(5)
                print(text.you_won)
                char.show_stats()
                sum_points(char)
                break
        if fight == "2" and char.cleverness >= 6:
            print("""You know you are not strong enough to fight the general. But there might be another way to 
            help the does and the rest of the rabbits. You remember passing a farm where you had heard some barking . . .
            """)
            while True:
                keep_going = input("Continue playing? Y/N")
                if keep_going == "Y":
                    break
                else:
                    print(text.ended)
                    exit()
            print("""There is only one way. With the help of Blackberry and Dandelion, you managed to 
            lead a hungry, angry dog towards the warren.
            """)

            print("""
            You are running as fast as you can! The crazy dog is dashing after you and 
            you can almost feel him nipping at your heels.""")

            while True:
                keep_going = input("Continue playing? Y/N")
                if keep_going == "Y":
                    break
                else:
                    print(text.ended)
                    exit()

            print("All of a sudden . . . ")

            while True:
                keep_going = input("Continue playing? Y/N")
                if keep_going == "Y":
                    break
                else:
                    print(text.ended)
                    exit()

        while True:
            val = random.choice(list(events.final_possibilities.items()))
            x, y = val
            print(y)
            if x == 1:
                while True:
                    keep_going = input("Continue playing? Y/N")
                    if keep_going == "Y":
                        break
                    else:
                        print(text.ended)
                        exit()
                print("""Fortunately, Dandelion comes to your aid and manages to get 
                the dog chasing him again. He gets back to Efafra, where the dog mauls
                General Woundwort to bits. The does are rescued!
                """)
                char.show_stats()
                print(text.you_won)
                sum_points(char)

                break
            elif x == 2:
                print(f"{char.name} has lost the game!")
                print(text.game_over)
                break
            elif x == 3:
                while True:
                    keep_going = input("Continue playing? Y/N")
                    if keep_going == "Y":
                        break
                    else:
                        print(text.ended)
                        exit()
                print("""The little girl who lives at the farm sees her 
                cat harrassing you. She comes out and chases the cat away. 
                She nurses you back to health, and several days later leaves
                you off at the corner of the road.
                """)
                while True:
                    keep_going = input("Continue playing? Y/N")
                    if keep_going == "Y":
                        break
                    else:
                        print(text.ended)
                        exit()
                print("""You return to the warren triumphant! The does have been 
                rescued and General Woundwort defeated.""")
                print(text.you_won)
                char.show_stats()
                sum_points(char)
                break
            elif x == 4:
                char.change_strength(4)
                char.change_cleverness(5)
                char.change_influence(5)
                print(f"{char.name} has won the game!")
                print(text.you_won)
                char.show_stats()
                sum_points(char)
                break
            elif x == 5:
                char.change_strength(4)
                char.change_cleverness(5)
                char.change_influence(5)
                print(f"{char.name} has won the game!")
                print(text.you_won)
                char.show_stats()
                sum_points(char)
                break
            break
