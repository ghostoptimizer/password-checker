# Password Strength & Feedback Checker
# Checks length, character variety, and common weak patterns
# Returns a score, label, and suggestions

COMMON_WORDS = ["password", "qwerty", "admin", "123456"]

def assess_password(pw):
    suggestions = []
    if not pw.strip():
        return 0, "Very Weak", ["Enter a non-empty password."]
    score = 0
    length = len(pw)
    if length >= 12: score += 40
    elif length >= 10: score += 30
    elif length >= 8: score += 20
    elif length >= 6: score += 10
    if any(c.islower() for c in pw): score += 10
    else: suggestions.append("Add lowercase letters.")
    if any(c.isupper() for c in pw): score += 10
    else: suggestions.append("Add uppercase letters.")
    if any(c.isdigit() for c in pw): score += 10
    else: suggestions.append("Add digits.")
    if any(not c.isalnum() for c in pw): score += 10
    else: suggestions.append("Add symbols.")
    if any(word in pw.lower() for word in COMMON_WORDS):
        score -= 20
        suggestions.append("Avoid common words.")
    if length < 12:
        suggestions.append("Increase length to at least 12 characters.")
    score = max(0, min(100, score))
    if score < 25: label = "Very Weak"
    elif score < 50: label = "Weak"
    elif score < 70: label = "Moderate"
    elif score < 85: label = "Strong"
    else: label = "Very Strong"
    return score, label, list(dict.fromkeys(suggestions))

def main():
    while True:
        pw = input("Enter a password: ")
        score, label, suggestions = assess_password(pw)
        print(f"Score: {score}/100, Strength: {label}")
        if suggestions:
            print("Suggestions:")
            for s in suggestions: print("-", s)
        if input("Try another? (yes/no): ").lower() not in ["y", "yes"]:
            break

if __name__ == "__main__":
    main()
