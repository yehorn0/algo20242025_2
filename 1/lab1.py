def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """
    $23.21 -> 23.21
    """
    pass


def percent_to_float(p: str) -> float:
    """
    50% -> 50.00
    """
    pass


if __name__ == "__main__":
    main()
