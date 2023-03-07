def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password
def decode(encoded_password): #daniel beeman
    password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password


def main():
    option = True
    while option:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = str(input())
            encoded_password = encode(password)
            print(encoded_password)
        if option == "2":
            encoded = str(input())
            decoded_password = decode(encoded)
            print(decoded_password)
        if option == "3":
            exit()



if __name__ == "__main__":
    main()