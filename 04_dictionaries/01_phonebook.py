def phonebook_app():
    phonebook = {}
    while True:
        name = input("Enter a new name to add (or press Enter to finish): ")
        if name == "":
            break
        phone = input(f"Enter phone number for {name}: ")
        if phone == "":
            break
        if name and phone:
            phonebook[name] = phone

    print("\n📞 Phonebook Created:", phonebook)

    while True:
        search_name = input("\nSearch a name to get the phone number (or press Enter to exit): ")
        if search_name == "":
            break
        if search_name in phonebook:
            print(f"{search_name}'s number is: {phonebook[search_name]}")
        else:
            print("❌ User not found!")


if __name__ == "__main__":
    phonebook_app()
