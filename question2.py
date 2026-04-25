def main() -> None:
    attendance_p: float = float(input("Enter attendance percentage (Without %): "))
    
    print(f"{"Eligible" if attendance_p >= 75 else "Not Eligible"}")


if __name__ == "__main__":
    main()