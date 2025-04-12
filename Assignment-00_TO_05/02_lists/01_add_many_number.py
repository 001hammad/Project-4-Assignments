numbers = []
user_num = input("How many numbers you want to add in the list? ")
user_number = int(user_num)

for i in range(user_number):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"Your list is: {numbers}")
print(f"The sum of the list is: {sum(numbers)}")
