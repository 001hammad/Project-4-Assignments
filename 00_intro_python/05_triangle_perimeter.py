#Here we create a logic that user input 3 sides of triangle and logic will show perimeter of triangle in cli

def main():
    a = input("What is the length of side 1? ")
    b = input("What is the length of side 2? ")
    c = input("What is the length of side 3? ")
    perimeter = float(a) + float(b) + float(c)
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()