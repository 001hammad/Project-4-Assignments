fruit_name = input("Enter fruit: ")
def check_stock(fruit_name):
    if fruit_name == 'banana':
        return 59
    elif fruit_name == 'mango':
        return 100
    elif fruit_name == 'apple':
        return 0
    else:
        return "shop closed!"


def main():
    result = check_stock(fruit_name)
    if result > 0:
        print(f"This fruit is in stock! Here is how many  {result}:")
    elif result == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is not available at all.")
main()