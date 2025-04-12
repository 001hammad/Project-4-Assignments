#Here we create a logic that user input thier fav animal and logic will show thier name in cli

def main():
    user_input = str(input("Enter your favourite animal: "))

    while not user_input.isalpha():
        print("Please enter a valid animal name.")
        user_input = str(input("Enter your favourite animal: "))

    if user_input:
        print(f"My favourite animal is {user_input}")
    else:
        print("You didn't enter anything!")


if __name__ == '__main__':
    main()



