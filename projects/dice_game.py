"""
Juego de dados
"""

import random


def roll_die(sides=6):
    return random.randint(1, sides)


def roll_dice(number=1, sides=6):
    results = [roll_die(sides) for _ in range(number)]
    return results


def play_dice():
    while True:
        try:
            number = int(input("How many dice do you want to roll? "))
            sides = int(input("How many sides do the dice have? "))
            if number < 1 or sides < 1:
                raise ValueError
        except ValueError:
            print("Please enter valid numbers greater than 0.")
            continue

        results = roll_dice(number, sides)
        print(f"Results: {', '.join(map(str, results))}")

        again = input("Do you want to roll again? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    play_dice()
