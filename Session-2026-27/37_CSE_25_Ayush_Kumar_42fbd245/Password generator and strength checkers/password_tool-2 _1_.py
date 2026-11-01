#!/usr/bin/env python3
"""Password Generator and Strength Checker.

Menu:
  1. Generate a password
  2. Check the strength of a password
  3. Exit
"""

import getpass
import math
import secrets
import string

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "admin", "welcome", "letmein",
    "monkey", "dragon", "football", "login", "passw0rd", "qwerty123",
}

SEQUENCES = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/"


# ---------- Generator ----------

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a cryptographically secure random password."""
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(SYMBOLS)

    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)}.")

    # Guarantee at least one character from each selected pool
    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


# ---------- Strength checker ----------

def has_sequence(password, run=3):
    """Detect runs like 'abc', '123', 'qwe' (forward or backward)."""
    p = password.lower()
    for seq in SEQUENCES:
        for s in (seq, seq[::-1]):
            for i in range(len(s) - run + 1):
                if s[i:i + run] in p:
                    return True
    return False


def has_repeats(password, run=3):
    """Detect the same character repeated, like 'aaa'."""
    return any(len(set(password[i:i + run])) == 1 for i in range(len(password) - run + 1))


def check_strength(password):
    """Return (score 0-100, label, feedback list, entropy bits)."""
    feedback = []
    score = 0
    length = len(password)

    # Length (up to 40 pts)
    score += min(length, 20) * 2
    if length < 8:
        feedback.append("Too short: use at least 12 characters.")
    elif length < 12:
        feedback.append("Better with 12+ characters.")

    # Character variety (up to 40 pts)
    checks = [
        (any(c.islower() for c in password), "lowercase letters"),
        (any(c.isupper() for c in password), "uppercase letters"),
        (any(c.isdigit() for c in password), "numbers"),
        (any(not c.isalnum() for c in password), "symbols"),
    ]
    for ok, name in checks:
        if ok:
            score += 10
        else:
            feedback.append(f"Add {name}.")

    # Unique characters (up to 20 pts)
    score += int(20 * len(set(password)) / max(length, 1))

    # Penalties
    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 5)
        feedback.append("This is a very common password. Avoid it!")
    if has_sequence(password):
        score -= 15
        feedback.append("Avoid sequences like 'abc', '123' or 'qwe'.")
    if has_repeats(password):
        score -= 15
        feedback.append("Avoid repeating the same character (e.g. 'aaa').")

    score = max(0, min(100, score))

    # Entropy estimate
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += 32
    entropy = length * math.log2(pool) if pool else 0

    if score < 30:
        label = "Very Weak"
    elif score < 50:
        label = "Weak"
    elif score < 70:
        label = "Medium"
    elif score < 85:
        label = "Strong"
    else:
        label = "Very Strong"

    if not feedback:
        feedback.append("Looks great. Keep it secret and unique per site.")

    return score, label, feedback, entropy


# ---------- CLI ----------

def ask_yes_no(prompt, default=True):
    hint = "Y/n" if default else "y/N"
    answer = input(f"{prompt} [{hint}]: ").strip().lower()
    if not answer:
        return default
    return answer.startswith("y")


def option_generate():
    try:
        raw = input("Password length (default 16): ").strip()
        length = int(raw) if raw else 16
        if length < 4 or length > 128:
            print("Please choose a length between 4 and 128.")
            return
    except ValueError:
        print("Invalid number.")
        return

    upper = ask_yes_no("Include uppercase letters?")
    digits = ask_yes_no("Include numbers?")
    symbols = ask_yes_no("Include symbols?")

    password = generate_password(length, upper, digits, symbols)
    print(f"\nGenerated password: {password}")
    score, label, _, entropy = check_strength(password)
    print(f"Strength: {label} ({score}/100, ~{entropy:.0f} bits of entropy)")


def option_check():
    password = getpass.getpass("Enter password to check (hidden input): ")
    if not password:
        print("No password entered.")
        return

    score, label, feedback, entropy = check_strength(password)
    print(f"\nStrength: {label} ({score}/100)")
    print(f"Estimated entropy: ~{entropy:.0f} bits")
    print("Feedback:")
    for tip in feedback:
        print(f"  - {tip}")


def main():
    while True:
        print("\n=== Password Tool ===")
        print("1. Generate a password")
        print("2. Check password strength")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            option_generate()
        elif choice == "2":
            option_check()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
