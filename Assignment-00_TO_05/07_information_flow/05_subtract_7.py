def subtract_seven(num):
    return num - 7

def main():
    while True:
        num = input("Enter num here: ")
        if num == "":
            break
        try:
            nums = int(num)
            result = subtract_seven(nums)
            print(result)
        except ValueError:
            print("Please enter a number, not text!")

        
main()
