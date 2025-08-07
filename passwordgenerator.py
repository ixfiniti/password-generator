import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[{]};:,<.>/?")

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_strength(password):
    length = len(password)
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[{]};:,<.>/?\\" for c in password):
        score += 1
    if length >= 12:
        score += 1

    # Determine strength level
    if score == 5:
        return "🟢 Very Strong"
    elif score == 4:
        return "🟡 Strong"
    elif score == 3:
        return "🟠 Moderate"
    elif score == 2:
        return "🔴 Weak"
    else:
        return "❌ Very Weak"

def main():
    print("🔐 Password Generator with Strength Rating\n")

    try:
        length = int(input("Enter password length (e.g., 12): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        strength = evaluate_strength(password)

        print(f"\nGenerated password: {password}")
        print(f"Password strength: {strength}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()