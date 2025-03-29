mylist = []
print("list before:", mylist)

def add_three_copies():
    message = input("Enter your message! ")
    for _ in range(3):
        mylist.append(message)
    print("list after:", mylist)

if __name__ == "__main__":
    add_three_copies()
print("proof:", mylist)