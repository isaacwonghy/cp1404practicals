minimum_length=8

def main():
    password = get_password(minimum_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Password?")
    while len(password) < minimum_length:
        print("Password too short!")
        password=input("Password?")
    return password

def print_asterisks(sequence):
    print("*" * len(sequence))

main()

