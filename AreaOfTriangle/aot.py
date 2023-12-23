def Tarea(base, height):
    return 0.5 * base * height


def main():
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))

        area = Tarea(base, height)
        print(f"The area of the triangle with base {base} and height {height} is {area} square units.")

    except ValueError:
        print("Invalid input! Please enter valid numerical values.")


if __name__ == "__main__":
    main()
