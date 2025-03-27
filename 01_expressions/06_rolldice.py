import random

num_sides = 6

def main():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    total = die1 + die2

    print(f"Dice have {num_sides} sides each.")
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    main()
