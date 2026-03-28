import utils
import os
from colorama import Fore

expense_categories = ["food", "entertainment", "education", "clothing", "travel", 
                      "subscriptions", "house", "gifts", "shopping", "health", 
                      "bills", "sports", "others"]

def input_expense(data):
    os.system("clear")
    utils.show_title()
    data.setdefault("expense", [])
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           ADD NEW EXPENSE")
    print(Fore.CYAN + "="*50)
    while True:
        category = utils.category_choice(expense_categories, "📝 Select the expense category or type 'done': ")
        if category == "done":
            break
        try:
            amount = float(input(Fore.WHITE + f"💰 Enter the expense amount for '{category}': "))
            print(Fore.BLUE + "-"*50)
        except ValueError:
            print(Fore.RED + "\n❌ Invalid amount! Please enter a number.")
            continue
        data["expense"].append({"Category": category, "Amount": amount})
        print(Fore.GREEN + f"\n✅ Added {amount:.2f} to '{category}' expenses.")

def remove_expense(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          REMOVE EXPENSE")
    print(Fore.CYAN + "="*50)
    data.setdefault("expense", [])
    utils.remove_items(data["expense"], "Category")

def update_expense(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          UPDATE EXPENSE")
    print(Fore.CYAN + "="*50)
    data.setdefault("expense", [])
    utils.update_items(data["expense"], "Category")

def total_expense(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          TOTAL EXPENSES")
    print(Fore.CYAN + "="*50)
    data.setdefault("expense", [])
    if not data["expense"]:
        print(Fore.YELLOW + "\n📭 No expenses recorded yet.")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return
    total = sum(item["Amount"] for item in data["expense"])
    print(Fore.MAGENTA + f"\n📊 Expense Summary:")
    print(Fore.CYAN + f"   • Total Expenses: {Fore.WHITE}{total:.2f}")
    print(Fore.MAGENTA + f"\n📋 Category Breakdown:")
    category_totals = {}
    for item in data["expense"]:
        cat = item["Category"]
        category_totals[cat] = category_totals.get(cat, 0) + item["Amount"]
    for category, amount in category_totals.items():
        print(Fore.CYAN + f"   • {category.capitalize()}: {Fore.WHITE}{amount:.2f}")
    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")