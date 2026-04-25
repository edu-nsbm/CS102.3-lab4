def main() -> None:
    num1: int = int(input("Enter number 1: "))
    num2: int = int(input("Enter number 2: "))
    num3: int = int(input("Enter number 3: "))

    if num1 == num2 and num2 == num3:
        print("All three numbers are equal.")
    elif num1 >= num2 and num1 >= num3:
        print(f"Max = {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"Max = {num2}")
    else:
        print(f"Max = {num3}")


if __name__ == "__main__":
    main()