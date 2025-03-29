def get_list(lst):
    while True:
        user_inp = input("Enter a value:  ")
        if user_inp == "":
            break
        lst.append(user_inp)
    print("Here's the list:" ,lst)

if __name__ == "__main__":
    my_list = []
    get_list(my_list)
