AFFERMATION = "I am capable of doing anything i put my mind to."
counter = 0
while True:
    user_inp = input("Enter affermation: ").lower()
    counter+=1
    if user_inp != AFFERMATION.lower():
        print("Wrong!😟")
    else:
        print(f"Right!🙂 btw you attemp {counter} time")
        break