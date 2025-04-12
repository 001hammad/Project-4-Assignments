def double_it(num:int):
    return num * 2

def number_double():
    user_num = int(input("Enter number here: "))
    num_times_2 = double_it(user_num)
    print(f"Double that is {num_times_2}")
number_double()