# PATHAGOROUS THEOREM
#Hypotenus^2 = AB^2 + AC^2
# PYTHAGOREAN THEOREM
# Hypotenuse² = AB² + AC²

import math

def main():
    try:
        user_ab = float(input("Enter the length of AB: "))
        user_ac = float(input("Enter the length of AC: "))
        hypotenuse = math.sqrt(user_ab ** 2 + user_ac ** 2)
        print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    except:
        print("Please enter a valid length!")

if __name__ == "__main__":
    main()
