MINIMUM_HEIGHT = 50


def tall_enough():
    try:
        while True:
            user_inp = input("How tall are you? ")
            if not user_inp:
                break
            user = int(user_inp)
            if user >= MINIMUM_HEIGHT:
                print("😀 You're tall enough to ride!")
            else:
                print("😟 You're not tall enough to ride, but maybe next year!")
    except ValueError:
        print("Invalid Input❌!")
if __name__ == "__main__":
    tall_enough()