#Here we write a program that like a ludo game random number genrate using random module in python

import random

def main():
    for i in range(3):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"Roll {i+1}: Die1 = {die1}, Die2 = {die2}")

if __name__ == '__main__':
    main()
