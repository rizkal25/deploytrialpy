import random

def generate_random_numbers():
    return [random.randint(100, 1000) for _ in range(50)]

if __name__ == "__main__":
    random_numbers = generate_random_numbers()
    print("Random Numbers:", random_numbers)