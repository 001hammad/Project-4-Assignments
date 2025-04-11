import random

num_generated = random.randint(1,99)
attemps = 0

while True:
    
    try:
        user_guess = int(input("Guess a number between 1 and 99 to win: "))
    except:
        print("Invalid input! Please enter a valid number.🚫")
        continue
    attemps +=1

    if user_guess < 1 or user_guess > 99:
        print("Please guess a number between 1 and 99.")
    elif user_guess > num_generated:
        print("Too High!")
    elif user_guess < num_generated:
        print("Too Low!")
    else:
        print(f"Congrats! You win in {attemps} attempts. The number was: {num_generated}")
        break