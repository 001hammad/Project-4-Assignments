import random

def done():
    if random.random() < 0.3:
        return True
    else:
        return False

def chaotic_counting():
    for i in range(1,11):
        if done():
            return
        else:
            print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
