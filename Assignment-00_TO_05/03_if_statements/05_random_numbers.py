import random

def generate_random_numbers():
    for _ in range(10):
        print(random.randint(1, 100), end=' ')

if __name__ == "__main__":
    generate_random_numbers()
