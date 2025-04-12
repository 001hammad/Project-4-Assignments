def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    return first_name , last_name, email

def main():
    user = get_user_info()
    print("Recieving following data: ",user)
main()