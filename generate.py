import random
import string

"""
    Generate a random 40-character hexadecimal address.

    This function generates a random Ethereum-like address consisting of 40
    hexadecimal characters.

    Returns:
        str: A randomly generated 40-character hexadecimal address.
"""
def generate_random_address():
    return ''.join(random.choices('0123456789abcdef', k=40))

"""
    Generate a random balance value between 0 and 9,999,999 million.

    This function generates a random integer representing an account balance
    within the range of 0 to 9,999,999.

    Returns:
        int: A random balance between 0 and 10 million.
 """
def generate_random_balance():
    return random.randint(0, 9_999_999)

"""
    Generate a text file with random addresses and balances.

    This function creates a file where each line consists of a random
    hexadecimal address and a corresponding random balance, separated by a space.
    Creates 100 addresses with balances and stores input.txt

    Returns:
        None: The function writes directly to the specified file.
"""
def generate():
    with open("input.txt", 'w') as f:
        for _ in range(100):
            address = generate_random_address()
            balance = generate_random_balance()
            f.write(f"{address} {balance}\n")
