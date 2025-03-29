my_list = []

while True:
    user = input("Enter value here: ")
    if user == "":
        break
    my_list.append(user)

print("Original List:", my_list)

MAX_LENGTH = 3

def get_list(lst):
    while len(lst) > MAX_LENGTH:
        deleted_elm = lst.pop()
        print("Removed:", deleted_elm)

if __name__ == "__main__":
    get_list(my_list)
