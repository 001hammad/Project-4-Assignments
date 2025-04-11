def calculate_total():
    fruits = {"apple": 10, "banana": 10, "mango": 10, "cherry": 15}
    total_amount = 0

    for fruit in fruits:
        user = input(f"How many ({fruit}) do you want? ")
        type_convertor = float(user)
        quantity = type_convertor * fruits[fruit]
        total_amount += quantity

    print(f"Your total bill: ${total_amount}")

if __name__ == "__main__":
    calculate_total()
