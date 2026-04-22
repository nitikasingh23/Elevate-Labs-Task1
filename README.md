# Elevate-Labs-Task1

# 🧮 Calculator CLI App

A simple command-line calculator built with Python that supports basic arithmetic operations. This project was built as part of a Python CLI mini-task to practice functions, loops, and user input handling.

---

## 📌 Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with divide-by-zero protection)
- 🔁 Loops continuously until the user chooses to exit
- ⚠️ Handles invalid inputs gracefully

---

## 🛠️ Tech Stack

| Tool      | Purpose              |
|-----------|----------------------|
| Python 3  | Core language        |
| VS Code   | Code editor          |
| Terminal  | Running the app      |

---

## 🚀 How to Run

### 1. Clone the Repository
bash
git clone https://github.com/your-username/calculator-cli.git
cd calculator-cli


### 2. Run the Script
bash
python calculator.py


> ✅ No external libraries needed — uses only built-in Python!

---

## 🖥️ Sample Output


👋 Welcome to the Calculator CLI App!

========================================
        🧮  CALCULATOR CLI APP
========================================
  Select an operation:
  1️⃣   Addition       (+)
  2️⃣   Subtraction    (-)
  3️⃣   Multiplication (*)
  4️⃣   Division       (/)
  5️⃣   Exit
========================================
  👉 Enter your choice (1-5): 1
  Enter first number  : 15
  Enter second number : 7

  📊 Result: 15.0 + 7.0 = 22.0


---

## 📂 Project Structure


calculator-cli/
│
├── calculator.py   # Main Python script
└── README.md       # Project documentation


---

## 💡 What I Learned / Did

### 🔹 1. Functions for Each Operation
Each arithmetic operation is written as a *separate function* (add, subtract, multiply, divide). This keeps the code clean and modular — each function does one job only.

python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b


### 🔹 2. User Input with input()
Used Python's built-in input() function to take choices and numbers from the user. Wrapped it inside a helper function get_number() with a try/except block to handle invalid inputs like letters or symbols.

python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")


### 🔹 3. Loop Until Exit
Used a while True loop to keep the calculator running. The loop only breaks when the user selects option *5 (Exit)*, which is a clean way to build interactive CLI apps.

python
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        break
    # ... rest of logic


### 🔹 4. Menu Display Function
Organized the UI into a show_menu() function so the display logic is separated from the calculation logic.

---

## 🧠 Key Concepts Used

- *Functions* — modular code design
- *while loop* — continuous program execution
- *try / except* — input validation and error handling
- *if / elif / else* — decision making based on user choice
- *f-strings* — clean, formatted output
