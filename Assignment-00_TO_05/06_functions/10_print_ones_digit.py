def print_ones_digit(num):
    ones = num % 10  # Modulo se ones digit milti hai
    print(f"The ones digit is {ones}")

def main():
    number = int(input("Enter a number: "))  # User se number lena
    print_ones_digit(number)  # Function call karna

if __name__ == '__main__':
    main()
