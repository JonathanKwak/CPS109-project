# Customizable Rock-Paper-Scissors Game
## Overview

This is a simple Rock-Paper-Scissors game implemented in Python. The twist: you can add your own elements and define which elements defeat others. This makes the game highly customizable and extendable beyond the classic rock, paper, scissors.
The game is user-friendly, with clear instructions and the ability to quit at any time.

## Features

Play a standard or customized version of Rock-Paper-Scissors.
Add or modify elements and their interactions via the data.txt file.
Friendly command-line interface.
Ability to quit at any time by typing QUIT.

## How It Works

- The game reads the data.txt file to determine which elements exist and how they interact.
- The user is prompted to select one of the available elements.
- The AI randomly selects an element.
- The winner is determined based on the rules defined in data.txt.
- The game repeats until the player chooses to quit.

## Setup
1. Make sure you have Python 3 installed.
2. Download or clone the project repository.
3. Ensure a `data.txt` file is present with the element rules.
4. Example format:
   ```
   ============
   Rock:Sponge,Scissors,Fire
   Paper:Rock,Water,Air
   Scissors:Sponge,Paper,Air
   Water:Rock,Scissors,Fire
   Air:Water,Fire,Rock
   Sponge:Water,Air,Paper
   ===========
   ```
6. Run the game.
   ```
   python game.py
   ```

## Example run
```
Select from the options: rock, paper or scissors
If you want to quit, type QUIT
>rock
=====================
Rock, Paper, Scissors...
Shoot!
AI rolled: scissors
You chose: rock
You won!
=====================
```

## Notes
- Element names are case-insensitive.
- Ensure your data.txt file is properly formatted to avoid errors.
- Ensure the 'data.txt' file is named 'data.txt'. Any other name will break the game.
