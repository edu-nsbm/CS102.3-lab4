def main() -> None:
    num1: int = int(input("Enter number 1: "))
    num2: int = int(input("Enter number 2: "))

    print(f"Before: {num1 = }, {num2 = }")

    num3 = num1
    num1 = num2
    num2 = num3

    print(f"After: {num1 = }, {num2 = }")


if __name__ == "__main__":
    main()