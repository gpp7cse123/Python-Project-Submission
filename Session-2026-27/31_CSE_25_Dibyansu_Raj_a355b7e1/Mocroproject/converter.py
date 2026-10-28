"""Number System Converter - Micro Project
Converts numbers between Decimal, Binary, Octal and Hexadecimal.
"""

DIGITS = "0123456789ABCDEF"
BASES = {
    "1": ("Decimal", 10),
    "2": ("Binary", 2),
    "3": ("Octal", 8),
    "4": ("Hexadecimal", 16),
}


def to_decimal(number: str, base: int) -> int:
    """Convert a string in the given base to a decimal integer."""
    number = number.strip().upper()
    if not number:
        raise ValueError("Input is empty.")

    value = 0
    for ch in number:
        if ch not in DIGITS[:base]:
            raise ValueError(f"'{ch}' is not a valid digit for base {base}.")
        value = value * base + DIGITS.index(ch)
    return value


def from_decimal(value: int, base: int) -> str:
    """Convert a decimal integer to a string in the given base."""
    if value == 0:
        return "0"

    result = ""
    while value > 0:
        result = DIGITS[value % base] + result
        value //= base
    return result


def convert(number: str, src: int, dst: int) -> str:
    """Convert a number from one base to another."""
    return from_decimal(to_decimal(number, src), dst)


def show_menu():
    print("=" * 44)
    print("         NUMBER SYSTEM CONVERTER")
    print("=" * 44)
    for key, (name, base) in BASES.items():
        print(f" {key}. {name} (base {base})")
    print(" 5. Exit")
    print("-" * 44)


def main():
    while True:
        show_menu()
        choice = input("Select INPUT number system (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the converter. Goodbye!")
            break

        if choice not in BASES:
            print("Invalid choice. Please enter 1-5.\n")
            continue

        src_name, src_base = BASES[choice]
        number = input(f"Enter the {src_name} number: ")

        try:
            decimal_value = to_decimal(number, src_base)
        except ValueError as err:
            print(f"Error: {err}\n")
            continue

        print(f"\nResults for {src_name} {number.strip().upper()}:")
        for _, (name, base) in BASES.items():
            print(f" {name:<12}: {from_decimal(decimal_value, base)}")
        print()


if __name__ == "__main__":
    main()
