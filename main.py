import json
from datetime import datetime

#Data file creating and reading
DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            content =  file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

#Addin expenses
def add_expense():
    amount = float(input("Eneter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")

    date_input =  input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if date_input.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = date_input
    
    #Expense JSON
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

#Viewing expenses by date
def view_by_date():
    date = input("Enter date (YYYY-MM-DD): ")

    expenses = load_expenses()
    results = [e for e in expenses if e['date'] == date]

    if not results:
        print("No expenses found for this date.")
    else:
        for e in results:
            print(f"{e['date']} - {e['category']}: ${e['amount']} - {e['description']}")

#Viewing expenses by category
def view_by_category():
    category = input("Enter category: ")

    expenses = load_expenses()
    results = [e for e in expenses if e['category'].lower() == category.lower()]

    if not results:
        print("No expenses found for this category.")
    else:
        for e in results:
            print(f"{e['date']} - {e['category']}: ${e['amount']} - {e['description']}")

#Viewing last X entries
def view_last_x_entries():
    x = int(input("Enter number of last entries to view: "))

    expenses = load_expenses()
    results = expenses[-x:]

    if not results:
        print("No expenses found.")
    else:
        for e in results:
            print(f"{e['date']} - {e['category']}: ${e['amount']} - {e['description']}")

#Viewing total spent
def view_total_spent():
    expenses = load_expenses()
    total = sum(e['amount'] for e in expenses)
    print(f"Total spent: ${total}")

def main():
    while True:
        print("1: Add expense")
        print("2: View by date")
        print("3: View by category")
        print("4: View last X entries")
        print("5: Toatal spent")
        print("6: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_by_date()
        elif choice == '3':
            view_by_category() 
        elif choice == '4':
            view_last_x_entries()
        elif choice == '5':
            view_total_spent()
        elif choice == '6':
            break

if __name__ == "__main__":
    main()