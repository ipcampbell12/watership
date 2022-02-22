"""All events are taken from this module"""


class Event:
    def __init__(self, fatigue, energy, influence):
        self.fatigue = fatigue
        self.energy = energy
        self.influence = influence


event1_op1 = Event(5, -40, -10)
event1_op2 = Event(1, -15, 10)
event2_op1 = Event(0, 35, 10)
event2_op2 = Event(3, -25, -5)
event3_op1 = Event(0, 15, 10)
event3_op2 = Event(0, 0, 0)

possibilities = {
    1: """
    The rabbits have time to rest,feed, and recover
    """,
    2: """
    Oh no! There's a fox! Run!
    """,
    3: """
    The sky darknens and before long a thunderstorm is upon you. 
    You had best find shelter soon.
    """,
    4: """
    One of Woundwort's wide patrolls has spotted you! Now he knows your coming.
    """,
    5: """You manage to pinch some vegetables from a nearby farm
    """
}

more_possibilities = {
    1: """
    You find a pea field to sleep in. Plenty of good food too!
    """,
    2: """
    Oh no! There's a stoat! Run!
    """,
    3: """
    The sun is so hot. The rabbits are gonna get cooked!
    """,
    4: """
    You had a little scuffle with a cat and won!
    """,
    5: """
    A farmer just saw you! Looks like he might be going for his gun . . .
    """
}

final_possibilities = {
    1: """
    The dog got distracted! You need him to keep chasing you!
    """,
    2: """
    The dog sinks its teeth into your heels. It's all over. 
    You are devoured, the rabbits scattered, and you have also lost. 
    """,
    3: """
    Blackberry has taken your place, and you are able to rest. 
    Sudenly, a cat is on top of you! Could this be the end???
    """,
    4: """
    The dog is led to Efafra and Woundwort is mauled to pieces. 
    The rabbits are saved!
    """,
    5: """
    The dog is led to Efafra and Woundwort flees as quick as he can. 
    The rabbits are saved!
    """

}

#val = random.choice(list(possibilities.items()))

#x, y = val
# print(x)
# print(y)


# print(val)
