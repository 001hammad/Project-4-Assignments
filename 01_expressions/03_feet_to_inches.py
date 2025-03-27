def main():
    try:
        user_feet = float(input("Enter number of feet :"))
        forInches = user_feet * 12
        print(f"{user_feet} feet is {forInches} inches.")
    except:
        print("Please Enter Valid Input")

if __name__ == "__main__":
    main()