import random 

problems = {
    "Are all the plurals correct in this phrase? \n\n At the zoo, we observed two elephant, three giraffes, and a lion.": "INCORRECT",
    "Are all the plurals correct in this sentence? \n\n She collected seashells, starfish, and a conch during her beach vacation.": "CORRECT",
    "Are all the plurals correct in this statement? \n\n The garden had rows of tomato, pepper, and bean plants.": "INCORRECT",
    "Are all the plurals correct in this question? \n\n How many tooth, teeth, and fangs does a vampire typically have?": "CORRECT",
    "Are all the plurals correct in this phrase? \n\n On the hike, we spotted a fox, two deer, and a raccoon.": "CORRECT",
    "Are all the plurals correct in this sentence? \n\n In the forest, there were mushrooms, ferns, and a deerskin.": "INCORRECT",
    "Are all the plurals correct in this statement? \n\n The library shelves were lined with old book, new magazine, and ancient scroll.": "INCORRECT",
    "Are all the plurals correct in this question? \n\n What are the differences between octopus, squid, and cuttlefish?": "CORRECT",
    "Are all the plurals correct in this phrase? \n\n At the party, there were balloons, streamers, and a confetti.": "INCORRECT",
    "Are all the plurals correct in this sentence? \n\n The display showcased antique doll, vintage toy, and modern gadget.": "INCORRECT",
    "Are all the plurals correct in this statement? \n\n The ocean exhibit had colorful fish, jellyfish, and a seashells.": "INCORRECT",
    "Are all the plurals correct in this question? \n\n How many moose, elk, and deer did you see on your camping trip?": "CORRECT",
    "Are all the plurals correct in this phrase? \n\n In the barn, there were horses, pig, and a chicken.": "INCORRECT",
    "Are all the plurals correct in this sentence? \n\n The package contained two book, a notebook, and a pen.": "INCORRECT",
    "Are all the plurals correct in this statement? \n\n The field had rows of corn, wheat, and barley plant.": "INCORRECT",
    "Are all the plurals correct in this question? \n\n Can you tell me the differences between goose, duck, and swan?": "CORRECT",
    "Are all the plurals correct in this phrase? \n\n During the expedition, they saw penguin, seal, and a walruses.": "INCORRECT",
    "Are all the plurals correct in this sentence? \n\n The orchard yielded apple, pear, and peach last season.": "INCORRECT",
    "Are all the plurals correct in this statement? \n\n The petting zoo featured rabbits, goat, and a pony.": "INCORRECT",
    "Are all the plurals correct in this question? \n\n How many sheep, goat, and llama live on the farm?": "CORRECT"
}




keys = list(problems.keys())
values = list(problems.values())

i = 0
action = "Go on!"

while action != "q":
    i = random.randint(0, len(keys) - 1)
    action = input(f"{keys[i]}\n \n \n Press Enter to reveal the answer, or 'q' to quit: ")
    if action.lower() == 'q':
        print("Quitting...")
        break

    print(f"The phrase is {values[i]}\n")
    print("\n")
    print("\n")
    action = input(f"Press Enter to see another one, or 'q' to quit: ")
    print("\n")
    print("\n")