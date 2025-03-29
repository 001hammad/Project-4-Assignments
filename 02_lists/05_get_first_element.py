def get_first_element(lst):
    if lst:  # ✅ Ensure list is not empty
        print("\n📌 First element in the list:", lst[0])
    else:
        print("\n⚠️ List is empty! No first element.")

if __name__ == "__main__":
    my_list = []
    
    print("🔢 Please enter elements (Press Enter to stop):")

    while True:
        user = input("👉 Enter an element: ")
        if user == "":  # ✅ If user presses enter, break loop
            break
        my_list.append(user)

    print("\n🧾 Full list of elements:", my_list)
    get_first_element(my_list)
