from expense import total_expense
from income_budget import total_income
from colorama import Fore
import os
import utils

def show_financial_summary(data):
    os.system("clear")
    utils.show_title()
    print(Fore.LIGHTYELLOW_EX + "\n" + "="*60)
    print(Fore.CYAN + "               FINANCIAL SUMMARY")
    print(Fore.LIGHTYELLOW_EX + "="*60)
    print(Fore.MAGENTA + "\n" + "~"*50)
    print(Fore.YELLOW + "           INCOME SUMMARY")
    print(Fore.MAGENTA + "~"*50)
    if not data.get("income"):
        print(Fore.YELLOW + "\n📭 No income recorded.")
        total_income_val = 0
    else:
        income_by_category = {}
        for item in data["income"]:
            income_by_category[item["Source"]] = (income_by_category.get(item["Source"], 0) + item["Amount"])
            
        total_income_val = sum(income_by_category.values())
        print(Fore.CYAN + f"\n📊 Total Income: {Fore.WHITE}{total_income_val:.2f}")
        print(Fore.MAGENTA + "\n📋 Income by Category:")
        print(Fore.BLUE + "-"*40)
        for category, amount in income_by_category.items():
            print(Fore.CYAN + f"   • {category.capitalize():15} : {Fore.WHITE}{amount:10.2f}")
    print(Fore.MAGENTA + "\n\n" + "^"*50)
    print(Fore.YELLOW + "           EXPENSE SUMMARY")
    print(Fore.MAGENTA + "="*50)
    if not data.get("expense"):
        print(Fore.YELLOW + "\n📭 No expenses recorded.")
        total_expense_val = 0
        expense_by_category = {}
    else:
        expense_by_category = {}
        for item in data["expense"]:
            expense_by_category[item["Category"]] = (
                expense_by_category.get(item["Category"], 0) + item["Amount"]
            )
        total_expense_val = sum(expense_by_category.values())
        print(Fore.CYAN + f"\n📊 Total Expenses: {Fore.WHITE}{total_expense_val:.2f}")
        print(Fore.MAGENTA + "\n📋 Expenses by Category:")
        print(Fore.BLUE + "-"*40)
        for category, amount in expense_by_category.items():
            print(Fore.CYAN + f"   • {category.capitalize():15} : {Fore.WHITE}{amount:10.2f}")
    print(Fore.MAGENTA + "\n\n" + "="*50)
    print(Fore.YELLOW + "        BUDGET vs EXPENSE ANALYSIS")
    print(Fore.MAGENTA + "="*50)
    if not data.get("budget"):
        print(Fore.YELLOW + "\n📭 No budget set.")
    else:
        budget_map = {b["Category"]: b["Budget"] for b in data["budget"]}
        matched = False
        print(Fore.BLUE + "\n" + "-"*70)
        print(Fore.CYAN + f"{'Category':15} | {'Budget':>10} | {'Spent':>10} | {'Difference':>12} | {'Status':15}")
        print(Fore.BLUE + "-"*70)
        for category, budget in budget_map.items():
            if category in expense_by_category:
                matched = True
                spent = expense_by_category[category]
                diff = budget - spent         
                if diff >= 0:
                    status = Fore.GREEN + "✅ Within Budget"
                else:
                    status = Fore.RED + "❌ Over Budget"            
                print(Fore.CYAN + f"{category.capitalize():15} | {Fore.WHITE}{budget:10.2f} | {Fore.WHITE}{spent:10.2f} | {Fore.WHITE}{diff:12.2f} | {status}")
        if not matched:
            print(Fore.YELLOW + "   No matching budget and expense categories found.")
    print(Fore.MAGENTA + "\n\n" + "~"*50)
    print(Fore.YELLOW + "           SAVINGS SUMMARY")
    print(Fore.MAGENTA + "~"*50)
    if not data.get("savings"):
        print(Fore.YELLOW + "\n📭 No savings recorded.")
        total_savings = 0
    else:
        savings_by_category = {}
        for item in data["savings"]:
            savings_by_category[item["Category"]] = (
                savings_by_category.get(item["Category"], 0) + item["Amount"]
            )
        total_savings = sum(savings_by_category.values())
        print(Fore.CYAN + f"\n📊 Total Savings: {Fore.WHITE}{total_savings:.2f}")
        print(Fore.MAGENTA + "\n📋 Savings by Category:")
        print(Fore.BLUE + "-"*40)
        for category, amount in savings_by_category.items():
            print(Fore.CYAN + f"   • {category.capitalize():15} : {Fore.WHITE}{amount:10.2f}")
    print(Fore.MAGENTA + "\n\n" + "="*50)
    print(Fore.YELLOW + "           SAVINGS GOALS")
    print(Fore.MAGENTA + "="*50)
    goals = data.get("savings_goal", {})
    if not goals:
        print(Fore.YELLOW + "\n📭 No savings goals set.")
    else:
        achieved_count = 0      
        print(Fore.CYAN + f"\n📋 Total Goals: {Fore.WHITE}{len(goals)}")
        print(Fore.BLUE + "-"*50)     
        for name, goal in goals.items():
            required = goal["required"]
            acquired = goal["acquired"]
            remaining = max(required - acquired, 0)
            progress = (acquired / required * 100) if required > 0 else 0       
            if goal["status"] == "achieved":
                achieved_count += 1
                status_icon = "✅"
                status_color = Fore.GREEN
            else:
                status_icon = "⏳"
                status_color = Fore.YELLOW         
            print(Fore.CYAN + f"\n📌 Goal: {Fore.WHITE}{name}")
            print(Fore.CYAN + f"   {status_color}{status_icon} Status: {goal['status'].capitalize()}")
            print(Fore.CYAN + f"   📊 Progress: {Fore.WHITE}{progress:.1f}%")
            print(Fore.CYAN + f"   💰 Required: {Fore.WHITE}{required:.2f}")
            print(Fore.CYAN + f"   💵 Acquired: {Fore.WHITE}{acquired:.2f}")
            print(Fore.CYAN + f"   📉 Remaining: {Fore.WHITE}{remaining:.2f}")
        print(Fore.GREEN + f"\n✅ Goals Achieved: {Fore.WHITE}{achieved_count}/{len(goals)}")
    print(Fore.MAGENTA + "\n\n" + "~"*50)
    print(Fore.YELLOW + "        LENT & BORROWED SUMMARY")
    print(Fore.MAGENTA + "~"*50)
    lent = []
    for item in data.get("lent", []):
        if item.get("Status") == "pending":
            lent.append(item)

    borrowed = []
    for item in data.get("borrowed", []):
        if item.get("Status") == "pending":
            borrowed.append(item)
    if not lent and not borrowed:
        print(Fore.YELLOW + "\n🎉 No pending lent or borrowed records.")
    else:
        if lent:
            total_lent = sum(item["Amount"] for item in lent)
            total_received = sum(item.get("Received", 0) for item in lent)
            pending_lent = total_lent - total_received   
            print(Fore.CYAN + f"\n📤 LENT SUMMARY:")
            print(Fore.CYAN + f"   • Total Lent: {Fore.WHITE}{total_lent:.2f}")
            print(Fore.CYAN + f"   • Total Received: {Fore.WHITE}{total_received:.2f}")
            print(Fore.CYAN + f"   • Pending to Receive: {Fore.WHITE}{pending_lent:.2f}")   
            print(Fore.MAGENTA + f"\n📋 Lent Records ({len(lent)}):")
            print(Fore.BLUE + "-"*50)
            for item in lent:
                remaining = item["Amount"] - item.get("Received", 0)
                status_icon = "✅" if item.get("Status") == "cleared" else "⏳"
                print(Fore.CYAN + f"   👤 {item['Person'].title():15} : {Fore.WHITE}{item['Amount']:8.2f} lent")
                print(Fore.CYAN + f"     💰 Received: {Fore.WHITE}{item.get('Received', 0):8.2f}")
                print(Fore.CYAN + f"     📊 Remaining: {Fore.WHITE}{remaining:8.2f}")
                print(Fore.CYAN + f"     📌 Status: {Fore.GREEN if item.get('Status') == 'cleared' else Fore.YELLOW}{status_icon} {item.get('Status', 'pending')}\n")
        if borrowed:
            total_borrowed = sum(item["Amount"] for item in borrowed)
            total_paid = sum(item.get("Paid", 0) for item in borrowed)
            pending_borrowed = total_borrowed - total_paid      
            print(Fore.CYAN + f"\n📥 BORROWED SUMMARY:")
            print(Fore.CYAN + f"   • Total Borrowed: {Fore.WHITE}{total_borrowed:.2f}")
            print(Fore.CYAN + f"   • Total Paid: {Fore.WHITE}{total_paid:.2f}")
            print(Fore.CYAN + f"   • Pending to Pay: {Fore.WHITE}{pending_borrowed:.2f}")     
            print(Fore.MAGENTA + f"\n📋 Borrowed Records ({len(borrowed)}):")
            print(Fore.BLUE + "-"*50)
            for item in borrowed:
                remaining = item["Amount"] - item.get("Paid", 0)
                status_icon = "✅" if item.get("Status") == "cleared" else "⏳"
                print(Fore.CYAN + f"   👤 {item['Person'].title():15} : {Fore.WHITE}{item['Amount']:8.2f} borrowed")
                print(Fore.CYAN + f"     💰 Paid: {Fore.WHITE}{item.get('Paid', 0):8.2f}")
                print(Fore.CYAN + f"     📊 Remaining: {Fore.WHITE}{remaining:8.2f}")
                print(Fore.CYAN + f"     📌 Status: {Fore.GREEN if item.get('Status') == 'cleared' else Fore.YELLOW}{status_icon} {item.get('Status', 'pending')}\n")
    print(Fore.MAGENTA + "\n" + "📊"*25)
    input(Fore.BLUE + "\nPress Enter to go back... ")