def main() -> None:
    bag_weight: float = float(input("Enter baggage weight: "))

    if bag_weight <= 20:
        print("No additional charges")
    elif bag_weight <= 30:
        print(f"Charges = {bag_weight * 200}")
    else:
        print("Bag Not Allowed!")


if __name__ == "__main__":
    main()