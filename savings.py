import utils
import os
from colorama import Fore


def add_savings(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            ADD SAVINGS")
    print(Fore.CYAN + "="*50)

    categories = ["salary", "gift", "business", "investments", "others"]
    print(Fore.MAGENTA + "\n📋 Select savings category:")
    for index, category in enumerate(categories, 1):
        print(Fore.CYAN + f"   {index}. {Fore.WHITE}{category.capitalize()}")
    print(Fore.BLUE + "-"*50)

    try:
        choice = int(input(Fore.WHITE + "👉 Enter category number: "))
        if choice < 1 or choice > len(categories):
            print(Fore.RED + "\n❌ Invalid selection.")
            return
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input. Please enter a number.")
        return

    category = categories[choice - 1]

    try:
        amount = float(input(Fore.WHITE + f"💰 Enter amount for {category.capitalize()}: "))
        if amount <= 0:
            print(Fore.RED + "\n❌ Amount must be greater than zero.")
            return
    except ValueError:
        print(Fore.RED + "\n❌ Invalid amount.")
        return

    data.setdefault("savings", [])
    data.setdefault("savings_history", [])

    data["savings"].append({
        "Category": category,
        "Amount": amount
    })

    data["savings_history"].append({
        "Category": category,
        "Amount": amount
    })

    print(Fore.GREEN + "\n✅ Savings added successfully!")
    print(Fore.CYAN + "="*50)


def remove_savings(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           REMOVE SAVINGS")
    print(Fore.CYAN + "="*50)

    if not data.get("savings"):
        print(Fore.YELLOW + "\n📭 No savings to remove.")
        print(Fore.CYAN + "="*50)
        return

    utils.remove_items(data["savings"], "Category")


def update_savings(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           UPDATE SAVINGS")
    print(Fore.CYAN + "="*50)

    if not data.get("savings"):
        print(Fore.YELLOW + "\n📭 No savings to update.")
        print(Fore.CYAN + "="*50)
        return

    utils.update_items(data["savings"], "Category")

def total_savings(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          TOTAL SAVINGS SUMMARY")
    print(Fore.CYAN + "="*50)

    if not data.get("savings"):
        print(Fore.YELLOW + "\n📭 No savings found.")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    total_saved = sum(item["Amount"] for item in data["savings"])

    print(Fore.MAGENTA + f"\n💰 Total Savings: {Fore.WHITE}{total_saved:.2f}")
    print(Fore.MAGENTA + f"📋 Number of Categories: {Fore.WHITE}{len(data['savings'])}")

    print(Fore.BLUE + "\n" + "-"*50)
    print(Fore.MAGENTA + "📊 Savings by Category:")
    print(Fore.BLUE + "-"*50)

    for item in data["savings"]:
        category = item["Category"]
        saved = item["Amount"]

        print(Fore.CYAN + f"\n   • {category.capitalize()}: {Fore.WHITE}{saved:.2f}")

    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")


def set_savings_goal(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          SET SAVINGS GOAL")
    print(Fore.CYAN + "="*50)

    data.setdefault("savings_goal", {})
    data.setdefault("goal_history", {})

    print(Fore.BLUE + "-"*50)
    goal_name = input(Fore.WHITE + "🎯 Enter a unique name for your savings goal: ").strip()

    if goal_name in data["savings_goal"]:
        print(Fore.RED + f"\n❌ A goal named '{goal_name}' already exists.")
        print(Fore.CYAN + "="*50)
        return

    try:
        required_amount = float(input(Fore.WHITE + f"💰 Enter required amount for '{goal_name}': "))
        acquired_amount = float(input(Fore.WHITE + f"💰 Enter already acquired amount for '{goal_name}': "))
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input. Please enter numbers only.")
        return

    status = "achieved" if acquired_amount >= required_amount else "pending"
    progress = (acquired_amount / required_amount * 100) if required_amount > 0 else 0

    data["savings_goal"][goal_name] = {
        "required": required_amount,
        "acquired": acquired_amount,
        "status": status
    }

    data["goal_history"].setdefault(goal_name, [])
    data["goal_history"][goal_name].append({
        "acquired": acquired_amount,
        "required": required_amount,
        "status": status
    })

    print(Fore.GREEN + f"\n✅ Savings goal '{goal_name}' set successfully!")
    print(Fore.CYAN + f"   • Required Amount: {Fore.WHITE}{required_amount:.2f}")
    print(Fore.CYAN + f"   • Acquired Amount: {Fore.WHITE}{acquired_amount:.2f}")
    print(Fore.CYAN + f"   • Progress: {Fore.WHITE}{progress:.1f}%")
    print(Fore.CYAN + f"   • Status: {Fore.GREEN if status == 'achieved' else Fore.YELLOW}{status.upper()}")
    print(Fore.CYAN + "="*50)

def update_goal(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          UPDATE SAVINGS GOAL")
    print(Fore.CYAN + "="*50)

    if not data.get("savings_goal"):
        print(Fore.YELLOW + "\n📭 No savings goals set yet.")
        print(Fore.CYAN + "="*50)
        return
    pending_goals = {
        name: goal for name, goal in data["savings_goal"].items()
        if goal["status"] == "pending"
    }
    if not pending_goals:
        print(Fore.GREEN + "\n🎉 All goals are already achieved!")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    goal_names = list(pending_goals.keys())

    print(Fore.MAGENTA + "\n🎯 Select a pending goal to update:")
    print(Fore.BLUE + "-"*50)
    for idx, goal_name in enumerate(goal_names, 1):
        goal = pending_goals[goal_name]
        progress = (goal["acquired"] / goal["required"] * 100) if goal["required"] > 0 else 0

        print(Fore.CYAN + f"   {idx}. {goal_name}")
        print(Fore.CYAN + f"      Required: {Fore.WHITE}{goal['required']:.2f} | Acquired: {Fore.WHITE}{goal['acquired']:.2f}")
        print(Fore.CYAN + f"      Progress: {Fore.WHITE}{progress:.1f}%")
        print()

    print(Fore.BLUE + "-"*50)

    try:
        choice = int(input(Fore.WHITE + "👉 Enter goal number: "))
        if choice < 1 or choice > len(goal_names):
            print(Fore.RED + "\n❌ Invalid selection.")
            return
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input.")
        return
    selected_goal = goal_names[choice - 1]
    goal = data["savings_goal"][selected_goal]

    try:
        add_amount = float(input(Fore.WHITE + f"💰 Enter amount to add to '{selected_goal}': "))
        if add_amount <= 0:
            print(Fore.RED + "\n❌ Amount must be greater than zero.")
            return
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input.")
        return

    goal["acquired"] += add_amount
    goal["status"] = "achieved" if goal["acquired"] >= goal["required"] else "pending"
    data.setdefault("goal_history", {})
    data["goal_history"].setdefault(selected_goal, [])
    data["goal_history"][selected_goal].append({
        "acquired": goal["acquired"],
        "required": goal["required"],
        "status": goal["status"]
    })

    progress = (goal["acquired"] / goal["required"] * 100) if goal["required"] > 0 else 0
    status_icon = "✅" if goal["status"] == "achieved" else "⏳"
    print(Fore.GREEN + f"\n✅ Goal '{selected_goal}' updated successfully!")
    print(Fore.CYAN + f"   • New Acquired Amount: {Fore.WHITE}{goal['acquired']:.2f}")
    print(Fore.CYAN + f"   • Progress: {Fore.WHITE}{progress:.1f}%")
    print(Fore.CYAN + f"   • Status: {status_icon} {goal['status']}")
    print(Fore.CYAN + "="*50)
