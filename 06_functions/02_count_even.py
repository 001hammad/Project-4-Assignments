num = []  # Empty list to store the numbers

def get_list_of_ints():
    while True:
        user_input = input("Enter number here: ")
        
        if user_input == "":  # If the user presses enter without typing, exit the loop
            break
        else:
            num.append(int(user_input))  # Convert the input to an integer and add to the list
    print(num)  # Print the final list after user exits the loop

def count_even():
    count = 0  # Variable to count even numbers
    for number in num:  # Loop through the list of numbers
        if number % 2 == 0:  # Check if the number is even
            count += 1  # Increment the count if the number is even
    print(f"Total even numbers: {count}")  # Print the count of even numbers

get_list_of_ints()  # Call the function to get numbers
count_even()  # Call the function to count even numbers
