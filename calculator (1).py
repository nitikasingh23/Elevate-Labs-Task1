# ============================================
#         Calculator CLI App
#         Built with Python 🐍
# ============================================

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers. Handles division by zero."""
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b

def get_number(prompt):
    """Helper to safely get a number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")

def show_menu():
    """Displays the calculator menu."""
    print("\n" + "=" * 40)
    print("        🧮  CALCULATOR CLI APP")
    print("=" * 40)
    print("  Select an operation:")
    print("  1️⃣   Addition       (+)")
    print("  2️⃣   Subtraction    (-)")
    print("  3️⃣   Multiplication (*)")
    print("  4️⃣   Division       (/)")
    print("  5️⃣   Exit")
    print("=" * 40)

def main():
    """Main function — runs the calculator loop."""
    print("\n👋 Welcome to the Calculator CLI App!")
    print("   Type a choice and press Enter.\n")

    while True:
        show_menu()
        choice = input("  👉 Enter your choice (1-5): ").strip()

        if choice == '5':
            print("\n✅ Thanks for using Calculator CLI! Goodbye! 👋\n")
            break

        if choice not in ('1', '2', '3', '4'):
            print("⚠️  Invalid choice! Please enter a number between 1 and 5.")
            continue

        # Get two numbers from the user
        num1 = get_number("  Enter first number  : ")
        num2 = get_number("  Enter second number : ")

        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operator = '/'

        # Display the result
        print(f"\n  📊 Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
