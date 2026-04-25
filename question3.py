def main() -> None:
    salary: float = float(input("Enter salary: "))
    bonus_p: float = 0

    if salary >= 100_000:
        bonus_p = 15
    elif salary >= 50_000:
        bonus_p = 10
    else:
        bonus_p = 5

    bonus: float = salary * bonus_p / 100
    salary += bonus
    # salary *= (100 + bonus_p) / 100

    print(f"{bonus_p = }, \n{bonus = }, \n{salary = }")


if __name__ == "__main__":
    main()