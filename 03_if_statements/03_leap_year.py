def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    user_year = input("Enter year: ")
    user = int(user_year)

    if is_leap_year(user):
        print("That's a leap year!")
    else:
        print("That's not a leap year!")
