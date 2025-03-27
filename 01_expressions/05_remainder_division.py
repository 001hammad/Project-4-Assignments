def main():
    try:
        user_num1 = int(input("Please enter an integer to be divide:"))
        user_num2 = int(input("Please enter an integer to divide by:"))
        division = user_num1 // user_num2
        reminder = user_num1 % user_num2
        print(f"The result of this division is {division} with a remainder of {reminder}")
    except ZeroDivisionError:
        print("0 is not divide by any value!")
    except:
        print("Enter Valid Input int!")

if __name__ == "__main__":
    main()