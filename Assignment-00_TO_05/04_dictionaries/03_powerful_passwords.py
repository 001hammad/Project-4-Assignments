from hashlib import sha256
stored_logins = {}
def hash_password(password:str):
    hashme = sha256(password.encode()).hexdigest()
    return hashme
stored_logins ["iamwho@gmail.com"] = hash_password("myhammad")

def login():
    while True:
        user_email = input("Enter your email: ")
        user_password = input("Enter your password: ")
        hashed_password = hash_password(user_password)
        if user_email == "":
            break
        if user_email in stored_logins:
            if stored_logins[user_email] == hashed_password:
                print("Login Successfull✅")
                break
            else:
                print("Login Failed Incorrect password!❌")
        else:
            print("Email not found!")
login()
