def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode(encoded_password):   # daniel beeman
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
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter you password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif option == "3":
            option = False


if __name__ == "__main__":
    main()
