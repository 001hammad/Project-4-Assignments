def count_numbers():
    number_counts = {}
    while True:
        user_input = input("Enter key: ")
        if user_input == '':
            break
        user = int(user_input)
        if user in number_counts:
            number_counts[user] += 1
        else:
            number_counts[user] = 1

    for key, value in number_counts.items(): 
        #.item() Dictionary ke saare key-value pairs ko ek-ek karke tuple form me deta hai
        # Taake aap unpe loop chala sako.
        print(f"{key} appears {value} times.")

if __name__ == "__main__":
    count_numbers()
