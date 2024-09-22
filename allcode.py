import random
import string


def random_address():
    return ''.join(random.choices('0123456789abcdef', k=40))

def random_balance():
    return random.randint(0, 9_999_999)

def generate(filename, num_entries):
    entries = [(random_address(), random_balance()) for _ in range(num_entries)]
    entries.sort(key=lambda x: x[0])
    with open(filename, 'w') as f:
        for address, balance in entries:
            f.write(f"{address} {balance}\0")

def prompt():
    # Prompt the user for a file path

    choice = input("Enter 'yes' to enter input file path, anything else will use our input.txt file: ")
    if(choice == 'yes'):
        file_path = input("Please enter the path to your text file: ")
    else:
        file_path = "./input.txt"

    generate(file_path, 100)

    return file_path



def createMerkleTree(file_path):
    try:
        # Open and read the text file
        with open(file_path, 'r') as file:
            content = file.read()


    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    file_path = prompt()
    createMerkleTree(file_path)
