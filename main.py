from generate import generate

def generate_random_address():
    return ''.join(random.choices('0123456789abcdef', k=40))

def generate_random_balance():
    return random.randint(0, 9_999_999)

def generate():
    with open("input.txt", 'w') as f:
        for _ in range(100):
            address = generate_random_address()
            balance = generate_random_balance()
            f.write(f"{address} {balance}\n")


def prompt():
    # Prompt the user for a file path
    file_path = input("Please enter the path to your text file: ")
    generate()

    try:
        # Open and read the text file
        with open(file_path, 'r') as file:
            content = file.read()


    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    prompt()
