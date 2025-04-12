#Here we create a logic that user get the square of any decimal or int number in cli

def main():
    num = float(input("Type a number to see its square: "))
    square = num ** 2
    print(f"{num} squared is {square}")

if __name__ == '__main__':
    main()