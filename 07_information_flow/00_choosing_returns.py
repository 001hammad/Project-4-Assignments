ADULT_AGE = 18
age = int(input("Enter your age: "))
def is_adult(age:int):
    if age >= ADULT_AGE:
        return "You are an adult!"
    else:
        return "You are not an adult!"
print(is_adult(age))
