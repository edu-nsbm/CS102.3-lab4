def main() -> None:
    min_end_balance: float = 500
    correct_pin: int = 1234

    balance: float = float(input("Enter balance: "))
    amount_w: float = float(input("Enter withdrawal amount: "))
    user_pin: int = int(input("Enter PIN: "))

    if user_pin == correct_pin:
        if balance - amount_w >= 500:
            balance -= amount_w
            print(f"Withdrawal of {amount_w} succeded!")
            print(f"Remaining balance: {balance}")
        else:
            print("Insufficient funds! Withdrawal unsucceded!")
    else:
        print("Invalid PIN. Two more attempts and your card's on-hold!")

if __name__ == "__main__":
    main()