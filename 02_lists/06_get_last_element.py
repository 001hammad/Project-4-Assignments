def get_last_element(lst):
    if lst:
        print("Last element in the list:" ,lst[-1])
    else:
        print("Your list is empty")

if __name__ == "__main__":
    my_list = []

    print("🔢 Please enter elements (Press Enter to stop):")
    while True:
        user_input = input("👉 Enter an element: ")
        if user_input == "":
            break
        my_list.append(user_input)

    print("\n🧾 Full list of elements:", my_list)
    get_last_element(my_list)
