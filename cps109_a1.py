"""

Must have all of these:
1. Conditions and decision making using if/else statements.
2. Working with sequences, such as lists, tuples, and strings.
3. Sequence iteration using for loops, general iteration using wile loops.
4. Importing namespaces, using their functions, writing your own functions.
5. Performing file I/O, reading input from a file, writing output to a file.

Problem:
Rock paper scissors is too boring. What if you could add more items?

"""

import time
import random

def parse_txt():
    """
    Interprets the data.txt file into something python can understand, specifically into the correct data types.
    """
    f = open("data.txt", "r")
    content = f.readlines()
    f.close()

    index = 0

    data = {}
    items = []
    recording = False

    while index < len(content):
        if "===" in content[index]:
            recording = not recording
            index += 1
            continue

        if recording:
            interpreted = content[index].strip().lower().split(":")
            victor = interpreted[0]
            loser = interpreted[1].split(",")

            # add items (Rock, Paper, whatever) into a set for later use
            if not victor in items:
                items.append(victor)

            data[victor] = loser
        
        index += 1
    
    return data, items

def translate_to_options(items: list[str]) -> str:
    """
    Gets the options and translates them into a human-readable string.

    Example: ["Rock", "Paper", "Scissors"] gets turned into "rock, paper or scissors"
    """

    final = ""

    for index in range(0, len(items)):
        item = items[index]

        if index == len(items) - 1:
            final += item.lower()
        elif index == len(items) - 2:
            final += item.lower() + " or "
        else:
            final += item.lower() + ", "
    
    return final

def translate_without_ors(items: list[str]) -> str:
    """
    Same thing as translate_to_options, except without the "or"
    """

    final = ""

    for index in range(0, len(items)):
        item = items[index]

        if index == len(items) - 1:
            final += item.lower()
        else:
            final += item.lower() + ", "
    
    return final[0].upper() + final[1:]

matches, items = parse_txt()

while True:
    print("Select from the options: " + translate_to_options(items))
    print("If you want to quit, type QUIT")

    AI_choice = items[random.randint(0, len(items) - 1)].lower()
    my_choice = input(">").lower().strip()

    if not my_choice in items:
        print("Invalid choice.")
        continue

    if my_choice == "quit":
        print("Quitting...")
        break

    print("=====================")
    print(translate_without_ors(items) + "...")
    time.sleep(1)
    print("Shoot!")

    print("AI rolled: " + AI_choice)
    print("You chose: " + my_choice)

    if my_choice in matches[AI_choice]:
        print("You lost!")
    elif AI_choice in matches[my_choice]:
        print("You won!")
    elif AI_choice == my_choice:
        print("It's a tie!")
    
    print("=====================")
    
    time.sleep(1)