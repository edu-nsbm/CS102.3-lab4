def main() -> None:
    st_gpa: float = float(input("Enter GPA: "))
    family_income: float = float(input("Enter family income: "))

    scholarship_level: str = "None"

    if st_gpa >= 3.5 and family_income < 30_000:
        scholarship_level = "Full"
    elif st_gpa >= 3.0 and family_income < 50_000:
        scholarship_level = "Partial"

    print(f"You are eligible for a {scholarship_level} Scholarship(s).")


if __name__ == "__main__":
    main()