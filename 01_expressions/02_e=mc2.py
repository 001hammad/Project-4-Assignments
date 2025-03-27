def main():
    try:
        user_mass = float(input("Enter kilos of mass: "))
        C = 299792458
        Energy = user_mass * C ** 2
        print("\ne = m * C^2...\n")
        print(f"m = {user_mass} kg")
        print(f"c = {C} m/s")
        print(f"{Energy} joules of energy!")
    except: 
        print("Please Enter A Number")

if __name__ == "__main__":
    main()