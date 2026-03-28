import utils
import os
from colorama import Fore

def add_lent(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            ADD LENT RECORD")
    print(Fore.CYAN + "="*50)
    person = input(Fore.WHITE + "👤 Enter person name: ").strip().lower()
    try:
        amount = float(input(Fore.WHITE + "💰 Enter lent amount: "))
    except ValueError:
        print(Fore.RED + "\n❌ Invalid amount. Please enter a number.")
        return
    
    data.setdefault("lent", [])
    for item in data["lent"]:
        if item["Person"] == person:
            print(Fore.YELLOW + "\n⚠️  This person already has a lent record.")
            return
    data["lent"].append({
        "Person": person,
        "Amount": amount,
        "Received": 0,
        "Status": "pending"})
    print(Fore.GREEN + f"\n✅ Lent record added successfully!")
    print(Fore.CYAN + f"   • Person: {Fore.WHITE}{person}")
    print(Fore.CYAN + f"   • Amount: {Fore.WHITE}{amount:.2f}")
    print(Fore.CYAN + f"   • Status: {Fore.YELLOW}pending")
    print(Fore.CYAN + "\n" + "="*50)

def add_borrowed(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           ADD BORROWED RECORD")
    print(Fore.CYAN + "="*50)
    person = input(Fore.WHITE + "👤 Enter lender name: ").strip().lower()
    try:
        amount = float(input(Fore.WHITE + "💰 Enter borrowed amount: "))
        print(Fore.BLUE + "-"*50)
    except ValueError:
        print(Fore.RED + "\n❌ Invalid amount. Please enter a number.")
        return
    data.setdefault("borrowed", []) 
    for item in data["borrowed"]:
        if item["Person"] == person:
            print(Fore.YELLOW + "\n⚠️  This person already has a borrowed record.")
            return  
    data["borrowed"].append({
        "Person": person,
        "Amount": amount,
        "Paid": 0,
        "Status": "pending"})
    print(Fore.GREEN + f"\n✅ Borrowed record added successfully!")
    print(Fore.CYAN + f"   • Lender: {Fore.WHITE}{person}")
    print(Fore.CYAN + f"   • Amount: {Fore.WHITE}{amount:.2f}")
    print(Fore.CYAN + f"   • Status: {Fore.YELLOW}pending")
    print(Fore.CYAN + "\n" + "="*50)

def update_lent(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           UPDATE LENT RECORD")
    print(Fore.CYAN + "="*50)

    data.setdefault("lent", [])

    if not data["lent"]:
        print(Fore.YELLOW + "\n📭 No lent records found.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    pending_records = []

    for item in data["lent"]:
        if item.get("Status") == "pending":
            pending_records.append(item)

    if not pending_records:
        print(Fore.YELLOW + "\n📭 No pending lent records.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    print(Fore.MAGENTA + "\nSelect a pending record:")
    for i, item in enumerate(pending_records, 1):
        remaining = item["Amount"] - item.get("Received", 0)
        print(Fore.CYAN + f"{i}. {item['Person'].title()}  (Remaining: {remaining:.2f})")

    try:
        index = int(input(Fore.WHITE + "\n👉 Enter choice number: ")) - 1
        item = pending_records[index]
    except (ValueError, IndexError):
        print(Fore.RED + "\n❌ Invalid selection.")
        return

    print(Fore.MAGENTA + "\n1. 📥 Add Received Amount")
    print(Fore.MAGENTA + "2. 💰 Update Total Lent Amount")
    print(Fore.BLUE + "\n" + "-"*50)

    choice = input(Fore.WHITE + "👉 Select option (1 or 2): ").strip()

    if choice == "1":
        try:
            received = float(input(Fore.WHITE + "💰 Enter amount received now: "))
        except ValueError:
            print(Fore.RED + "\n❌ Invalid amount.")
            return

        remaining = item["Amount"] - item["Received"]

        if received > remaining:
            print(Fore.RED + f"\n❌ You can only receive up to {remaining:.2f}")
            return

        item["Received"] += received
        item["Status"] = "cleared" if item["Received"] >= item["Amount"] else "pending"

        print(Fore.GREEN + "\n✅ Payment received updated!")

    elif choice == "2":
        try:
            new_amount = float(input(Fore.WHITE + "💰 Enter new total lent amount: "))
        except ValueError:
            print(Fore.RED + "\n❌ Invalid amount.")
            return

        item["Amount"] = new_amount
        item["Status"] = "cleared" if item["Received"] >= new_amount else "pending"

        print(Fore.GREEN + "\n✅ Lent amount updated!")

    else:
        print(Fore.RED + "\n❌ Invalid choice.")

def update_borrowed(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          UPDATE BORROWED RECORD")
    print(Fore.CYAN + "="*50)

    data.setdefault("borrowed", [])

    if not data["borrowed"]:
        print(Fore.YELLOW + "\n📭 No borrowed records found.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    print(Fore.MAGENTA + "\nSelect a record:")
    pending_records = []

    for item in data["borrowed"]:
        if item.get("Status") == "pending":
            pending_records.append(item)

    if not pending_records:
        print(Fore.YELLOW + "\n📭 No pending borrowed records.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    print(Fore.MAGENTA + "\nSelect a pending record:")
    for i, item in enumerate(pending_records, 1):
        remaining = item["Amount"] - item.get("Paid", 0)
        print(Fore.CYAN + f"{i}. {item['Person'].title()}  (Remaining: {remaining:.2f})")


    try:
        index = int(input(Fore.WHITE + "\n👉 Enter choice number: ")) - 1
        item = pending_records[index]
    except (ValueError, IndexError):
        print(Fore.RED + "\n❌ Invalid selection.")
        return

    print(Fore.MAGENTA + "\n1. 💳 Add Paid Amount")
    print(Fore.MAGENTA + "2. 💰 Update Total Borrowed Amount")
    print(Fore.BLUE + "\n" + "-"*50)

    choice = input(Fore.WHITE + "👉 Select option (1 or 2): ").strip()

    if choice == "1":
        try:
            paid = float(input(Fore.WHITE + "💰 Enter amount paid now: "))
        except ValueError:
            print(Fore.RED + "\n❌ Invalid amount.")
            return

        remaining = item["Amount"] - item["Paid"]

        if paid > remaining:
            print(Fore.RED + f"\n❌ You can only pay up to {remaining:.2f}")
            return

        item["Paid"] += paid
        item["Status"] = "cleared" if item["Paid"] >= item["Amount"] else "pending"

        print(Fore.GREEN + "\n✅ Payment updated!")

    elif choice == "2":
        try:
            new_amount = float(input(Fore.WHITE + "💰 Enter new total borrowed amount: "))
        except ValueError:
            print(Fore.RED + "\n❌ Invalid amount.")
            return

        item["Amount"] = new_amount
        item["Status"] = "cleared" if item["Paid"] >= new_amount else "pending"

        print(Fore.GREEN + "\n✅ Borrowed amount updated!")

    else:
        print(Fore.RED + "\n❌ Invalid choice.")


def remove_lent(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           REMOVE LENT RECORD")
    print(Fore.CYAN + "="*50)

    data.setdefault("lent", [])

    pending_records = []
    for item in data["lent"]:
        if item.get("Status") == "pending":
            pending_records.append(item)

    if not pending_records:
        print(Fore.YELLOW + "\n📭 No pending lent records to remove.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    utils.remove_items(pending_records, "Person")

    new_list = []
    for item in data["lent"]:
        if item.get("Status") == "cleared" or item in pending_records:
            new_list.append(item)

    data["lent"] = new_list
    print(Fore.GREEN + "\n" + "~"*50)
    print(Fore.YELLOW + "      Pending lent removal completed!")
    print(Fore.GREEN + "~"*50)

def remove_borrowed(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          REMOVE BORROWED RECORD")
    print(Fore.CYAN + "="*50)
    data.setdefault("borrowed", [])

    pending_records = []
    for item in data["borrowed"]:
        if item.get("Status") == "pending":
            pending_records.append(item)

    if not pending_records:
        print(Fore.YELLOW + "\n📭 No pending borrowed records to remove.")
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    utils.remove_items(pending_records, "Person")

    new_list = []
    for item in data["borrowed"]:
        if item.get("Status") == "cleared" or item in pending_records:
            new_list.append(item)

    data["borrowed"] = new_list
    print(Fore.GREEN + "\n" + "~"*50)
    print(Fore.YELLOW + "      Pending borrowed removal completed!")
    print(Fore.GREEN + "~"*50)


def total_lent(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           TOTAL LENT SUMMARY")
    print(Fore.CYAN + "="*50)

    data.setdefault("lent", [])

    total = sum(item["Amount"] for item in data["lent"])
    received = sum(item.get("Received", 0) for item in data["lent"])

    print(Fore.CYAN + f"\n💰 Total Lent: {Fore.WHITE}{total:.2f}")
    print(Fore.CYAN + f"📥 Total Received: {Fore.WHITE}{received:.2f}")
    print(Fore.CYAN + f"⏳ Remaining: {Fore.WHITE}{total - received:.2f}")

    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")

def total_borrowed(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "          TOTAL BORROWED SUMMARY")
    print(Fore.CYAN + "="*50)

    data.setdefault("borrowed", [])

    total = sum(item["Amount"] for item in data["borrowed"])
    paid = sum(item.get("Paid", 0) for item in data["borrowed"])

    print(Fore.CYAN + f"\n💰 Total Borrowed: {Fore.WHITE}{total:.2f}")
    print(Fore.CYAN + f"💳 Total Paid: {Fore.WHITE}{paid:.2f}")
    print(Fore.CYAN + f"⏳ Remaining: {Fore.WHITE}{total - paid:.2f}")

    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")


def lent_history(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "            LENT HISTORY")
    print(Fore.CYAN + "="*50)

    data.setdefault("lent", [])

    cleared_records = []
    for item in data["lent"]:
        if item.get("Status") == "cleared":
            cleared_records.append(item)

    if not cleared_records:
        print(Fore.YELLOW + "\n📭 No cleared lent records found.")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    print(Fore.MAGENTA + f"\n📋 Total Records: {Fore.WHITE}{len(cleared_records)}")
    print(Fore.BLUE + "\n" + "-"*50)

    for i, item in enumerate(cleared_records, 1):
        remaining = item["Amount"] - item.get("Received", 0)
        print(Fore.CYAN + f"\n📌 Record #{i}:")
        print(Fore.CYAN + f"   • Person: {Fore.WHITE}{item['Person'].title()}")
        print(Fore.CYAN + f"   • Amount Lent: {Fore.WHITE}{item['Amount']:.2f}")
        print(Fore.CYAN + f"   • Received: {Fore.WHITE}{item.get('Received', 0):.2f}")
        print(Fore.CYAN + f"   • Remaining: {Fore.WHITE}{remaining:.2f}")
        print(Fore.CYAN + f"   • Status: {Fore.GREEN}✅ cleared")

    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")


def borrowed_history(data):
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           BORROWED HISTORY")
    print(Fore.CYAN + "="*50)

    data.setdefault("borrowed", [])

    cleared_records = []
    for item in data["borrowed"]:
        if item.get("Status") == "cleared":
            cleared_records.append(item)

    if not cleared_records:
        print(Fore.YELLOW + "\n📭 No cleared borrowed records found.")
        print(Fore.CYAN + "="*50)
        input(Fore.BLUE + "\nPress Enter to go back... ")
        return

    print(Fore.MAGENTA + f"\n📋 Total Records: {Fore.WHITE}{len(cleared_records)}")
    print(Fore.BLUE + "\n" + "-"*50)

    for i, item in enumerate(cleared_records, 1):
        remaining = item["Amount"] - item.get("Paid", 0)
        print(Fore.CYAN + f"\n📌 Record #{i}:")
        print(Fore.CYAN + f"   • Lender: {Fore.WHITE}{item['Person'].title()}")
        print(Fore.CYAN + f"   • Amount Borrowed: {Fore.WHITE}{item['Amount']:.2f}")
        print(Fore.CYAN + f"   • Paid: {Fore.WHITE}{item.get('Paid', 0):.2f}")
        print(Fore.CYAN + f"   • Remaining: {Fore.WHITE}{remaining:.2f}")
        print(Fore.CYAN + f"   • Status: {Fore.GREEN}✅ cleared")

    print(Fore.CYAN + "\n" + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")
