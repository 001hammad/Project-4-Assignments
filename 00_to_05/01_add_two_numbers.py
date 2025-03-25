#Here we add 2 numbers and print the sum of them according to user input

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print(f"Sum of the {num1} + {num2} is: ", sum)

if __name__ == '__main__':
    main()
