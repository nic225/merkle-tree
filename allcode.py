import random
import string
import hashlib

def random_address():
    return ''.join(random.choices('0123456789abcdef', k=40))

def random_balance():
    return random.randint(0, 9_999_999)

def generate(filename, num_entries):
    entries = [(random_address(), random_balance()) for _ in range(num_entries)]
    entries.sort(key=lambda x: x[0])
    with open(filename, 'w') as f:
        for address, balance in entries:
            f.write(f"{address} {balance}\0\n")

def prompt():
    choice = input("Enter 'yes' to enter input file path, anything else will use our input.txt file: ")
    if(choice == 'yes'):
        file_path = input("Please enter the path to your text file: ")
    else:
        file_path = "./input.txt"

    #generate(file_path, 100)

    return file_path

def get_accounts(filename):
    accounts = []
    try: 
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\0')
            for line in lines:
                if line.strip():  # Ignore empty lines
                    address, balance = line.split(' ')
                    account = (address, balance)
                    accounts.append(account)
    
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return accounts

class MerkleNode:
    def __init__(self, left_node=None, right_node=None, account=None, balance=None):
        self.left = left_node
        self.right = right_node
        if self.right and self.left:
            self.hash = self.calculate_parent_hash()
        elif self.left:
            self.hash = self.left.hash

        if account is not None and balance is not None:
            self.account = account
            self.balance = balance
            self.hash = self.calculate_hash(account, balance)


    def calculate_hash(self, account, balance):
        data = f"{account}{balance}".encode()
        return hashlib.sha256(data).hexdigest()

    def calculate_parent_hash(self):
        combined_hash = self.left.hash + self.right.hash
        return hashlib.sha256(combined_hash.encode()).hexdigest()

def get_root(nodes):
    parents = []
    n = len(nodes)
    for i in range(0, n, 2):
        if i + 1 < n:
            parents.append(MerkleNode(left_node=nodes[i], right_node=nodes[i + 1]))
        else:
            parents.append(nodes[i])

    if len(parents) == 1:
        return parents[0].hash
    else:
        return get_root(parents)

def createMerkleTree(file_path):
    accounts = get_accounts(file_path)
    leaf_nodes = [MerkleNode(account=account, balance=balance) for account, balance in accounts]
    root = get_root(leaf_nodes)
    return root

if __name__ == "__main__":
    file_path = prompt()
    print("Merkle Root: " + createMerkleTree(file_path))
