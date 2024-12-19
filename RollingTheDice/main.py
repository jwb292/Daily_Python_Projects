# This project simulates a dice roll by generating a random number between 1 and 6. Each time the program runs, it "rolls the dice" and displays the result. This project introduces students to working with random numbers and basic output formatting.

import random

diceRoll1 = random.randint(1, 6)
diceRoll2 = random.randint(1, 6)
print(f"You rolled a {diceRoll1} and {diceRoll2}")