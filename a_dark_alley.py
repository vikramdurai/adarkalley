from time import sleep
from random import randint

# a style of printing the words
def print_st(words):
    for char in words:
        sleep(0.07)
        print(char, end='', flush=True)
    print()

start = ["Welcome! This is A Dark Alley, a game primarily inspired by ADarkRoom and choice-based games.",
    "To start the text adventure, press Enter. Press Ctrl+C to exit."
    ]
for i in start:
    print_st(i)
try:
    cont = input()
except KeyboardInterrupt:
    print_st("Bye!")
    exit()

story_path_1 = [
    "You're walking down a dark alley. You don't remember who you are, where you're from or how you got here.",
    "You wonder why nobody else is here. It's eerily quiet.",
    "You feel hungry. There are some trash cans. There is also a cat moving stealthily out of the alley.",
]

hunger = 1

for i in story_path_1:
    print_st(i)

print_st("To choose, type the number of the choice you wanted.")
print_st("[1] Scrounge the trash cans for food")
print_st("[2] Follow the cat")

c = input("> ")
if c in ["1", "one"]:
    path_var = "trash"
elif c in ["2", "two"]:
    path_var = "cat"
else:
    glitch = [
        "You decide to fly on the wings of your imagination.",
        "You walk out of the alley."
    ]
    for i in glitch:
        print_st(i)
    sleep(2)
    print_st("You are promptly hit by a truck.")
    print_st("~ THE END ~")
    print_st("Score: 0")
    print_st("Game created by Vikram Durai. Twitter: @vikramsworld, Instagram: @vikramsinstaacount,")
    exit()

if path_var == "trash":
    rc = randint(1, 100)
    if rc > 50:
        story_event = [
            "You rummaged the trash. It didn't contain any food."
            "You decided to follow the cat."
        ]
        for i in story_event:
            print_st(i)
        path_var = "cat"
    else:
        print_st("yo")
else:
    story_path_2_p1 = [
        "You follow the cat through twisted twilight shadows.",
        "Your hunger ever gnaws at you.",
        "Suddenly, the cat crawls near your feet, and drops a slimy item.",
        "You just ate a fish. Your hunger has been reset."
        ]
    for i in story_path_2_p1:
        print_st(i)
        hunger = 0
                        
    sleep(2)
    story_path_2_p2 = [
        "..The cat seems to have taken a liking to you.",
        "You have now got a friend. It lies purring contentedly on your lap.",
        "He will be with you wherever you go.",
    ]
    for i in story_path_2_p2:
        print_st(i)
        
    sleep(1)
    story_path_3_p3 = [
        "There are four directions for you to go to.",
        "West of you lies the highway.",
        "North, as you can see, houses the apartments.",
        "South lies a canopy of concrete.",
        "East is the railway."
    ]        



        
