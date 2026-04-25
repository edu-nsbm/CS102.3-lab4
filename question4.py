def main() -> None:
    income: float = float(input("Enter income: "))
    tax_p: float = 0

    if income >= 100_000:
        tax_p = 20
    elif income >= 50_000:
        tax_p = 10
    else:
        tax_p = 0

    tax: float = income * tax_p / 100

    print(f"{income = }, \n{tax_p = }, \n{tax = }")


if __name__ == "__main__":
    main()