import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 20
        feedback.append(("Length (8+ characters)", True))
    else:
        feedback.append(("Length (8+ characters)", False))

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 20
        feedback.append(("Uppercase Letter", True))
    else:
        feedback.append(("Uppercase Letter", False))

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 20
        feedback.append(("Lowercase Letter", True))
    else:
        feedback.append(("Lowercase Letter", False))

    # Number
    if re.search(r"\d", password):
        score += 20
        feedback.append(("Number", True))
    else:
        feedback.append(("Number", False))

    # Special Character
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 20
        feedback.append(("Special Character", True))
    else:
        feedback.append(("Special Character", False))

    # Strength Category
    if score == 100:
        strength = "Very Strong 💪"
    elif score >= 80:
        strength = "Strong ✅"
    elif score >= 60:
        strength = "Medium ⚠️"
    elif score >= 40:
        strength = "Weak ❌"
    else:
        strength = "Very Weak 🚫"

    return score, strength, feedback


def suggest_improvements(feedback):
    print("\nSuggestions:")
    has_suggestion = False

    for item, status in feedback:
        if not status:
            has_suggestion = True
            print(f"• Add {item.lower()}.")

    if not has_suggestion:
        print("Excellent! No improvements needed.")


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter Password: ")

    score, strength, feedback = check_password_strength(password)

    print("\nPassword Analysis")
    print("-" * 40)

    for item, status in feedback:
        symbol = "✔" if status else "✘"
        print(f"{symbol} {item}")

    print("-" * 40)
    print(f"Strength : {strength}")
    print(f"Score    : {score}/100")

    suggest_improvements(feedback)


if __name__ == "__main__":
    main()