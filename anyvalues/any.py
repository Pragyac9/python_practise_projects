import random


def main():
    try:

        value = int(input("Enter the maximum value for the random number: "))

        random_num = random.randint(0, value)

        print(f"Random number is  : {random_num}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
