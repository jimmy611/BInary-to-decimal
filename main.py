def decimal_to_binary(decimal_num):
    """Converts a decimal number to binary.

    Parameters:
    decimal_num (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the decimal number.
    """
    binary_num = bin(decimal_num)[2:]  # Convert to binary and remove the '0b' prefix
    return binary_num


def binary_to_decimal(binary_num):
    """Converts a binary number to decimal.

    Parameters:
    binary_num (str): The binary number to be converted.

    Returns:
    int: The decimal representation of the binary number.
    """
    decimal_num = int(binary_num, 2)  # Convert binary to decimal
    return decimal_num


def main():
    print("Decimal to Binary and Vice Versa Converter")

    while True:
        print("\nChoose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            decimal_num = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(decimal_num)
            print(f"Binary representation: {binary_result}")

        elif choice == '2':
            binary_num = input("Enter a binary number: ")
            decimal_result = binary_to_decimal(binary_num)
            print(f"Decimal representation: {decimal_result}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
