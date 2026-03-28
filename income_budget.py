import utils
import os
from colorama import Fore

income_categories = ["salary", "gift", "business", "investments", "others"]

def input_income(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            ADD NEW INCOME")
    print(Fore.CYAN + "="*50)
    while True:
        source = utils.category_choice(income_categories, "📝 Select the income source or type 'done': ")
        if source == "done":
            break
        try:
            amount = float(input(Fore.WHITE + f"💰 Enter amount for '{source}': "))
            data.setdefault("income", []).append({"Source": source, "Amount": amount})
            print(Fore.GREEN + f"\n✅ Added {amount:.2f} to '{source}' income.")
        except ValueError:
            print(Fore.RED + "\n❌ Please enter a valid number.")

def remove_income(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            REMOVE INCOME")
    print(Fore.CYAN + "="*50)
    data.setdefault("income", [])
    utils.remove_items(data["income"], "Source")

def update_income(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            UPDATE INCOME")
    print(Fore.CYAN + "="*50) 
    data.setdefault("income", [])
    utils.update_items(data["income"], "Source")

def total_income(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           TOTAL INCOME")
    print(Fore.CYAN + "="*50)
    data.setdefault("income", [])
    if not data["income"]:
        print(Fore.YELLOW + "\n📭 No income recorded yet.")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return
    total = 0
    for item in data["income"]:
        total += item["Amount"]
    print(Fore.MAGENTA + f"\n📊 Income Summary:")
    print(Fore.CYAN + f"   • Total Income: {Fore.WHITE}{total:.2f}")
    print(Fore.MAGENTA + f"\n📋 Source Breakdown:")
    source_totals = {}
    for item in data["income"]:
        src = item["Source"]
        source_totals[src] = source_totals.get(src, 0) + item["Amount"]
    for source, amount in source_totals.items():
        print(Fore.CYAN + f"   • {source.capitalize()}: {Fore.WHITE}{amount:.2f}")
    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")

budget_categories = [
    "food", "entertainment", "education", "clothing", "travel",
    "subscriptions", "house", "gifts", "shopping", "health",
    "bills", "sports", "others"]

def input_budget(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            SET BUDGET")
    print(Fore.CYAN + "="*50)
    while True:
        category = utils.category_choice(budget_categories, "📝 Select the budget category or type 'done': ")
        if category == "done":
            break    
        try:
            budget = float(input(Fore.WHITE + f"💰 Enter the budget for '{category}': "))
            data.setdefault("budget", []).append({"Category": category, "Budget": budget})
            print(Fore.GREEN + f"\n✅ Set budget of {budget:.2f} for '{category}'.")
        except ValueError:
            print(Fore.RED + "\n❌ Please enter a valid number.")

def remove_budget(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            REMOVE BUDGET")
    print(Fore.CYAN + "="*50)
    data.setdefault("budget", [])
    utils.remove_items(data["budget"], "Category")

def update_budget(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            UPDATE BUDGET")
    print(Fore.CYAN + "="*50)
    data.setdefault("budget", [])
    utils.update_items(data["budget"], "Category")