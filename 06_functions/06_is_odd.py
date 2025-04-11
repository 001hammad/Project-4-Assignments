def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2
    return remainder == 1

def main():
    for i in range(10, 20):  
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

if __name__ == '__main__':
    main()
