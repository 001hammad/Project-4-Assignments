#Here we create a logic that user input temprature in farhenheit and logic will show temprature in celcius in cli

def main():
    farhenheit  = float(input("Enter the temprature in farhenheit: "))
    celcius = (farhenheit - 32) * 5.0/9.0
    print(f"{farhenheit}f Temprature in celcius is: : {round(celcius,2)}c")
    
if __name__ == '__main__':
    main()