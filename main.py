from generate import generate

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
