import income_budget 
import expense 
import auth 
import os
import utils
import savings 
import lent_borrowed 
import summary  
import calculator
import recommendations
from colorama import Fore
from storage import read_data, save_data, set_current_user  

def income_budget_menu(data):
    os.system("clear")
    utils.show_title()
    while True:
        print(Fore.LIGHTYELLOW_EX + "\n" + "="*50)
        print(Fore.CYAN + "        INCOME & BUDGET MENU")
        print(Fore.LIGHTYELLOW_EX + "="*50)
        print(Fore.WHITE + "\n1. Add Income          |   2. Remove Income")
        print(Fore.WHITE + "3. Update Income       |   7. Total Income")
        print(Fore.WHITE + "\n4. Add Budget          |   5. Remove Budget") 
        print(Fore.WHITE + "6. Update Budget       |")
        print(Fore.BLUE + "\n" + "-"*50)
        print(Fore.YELLOW + "8. Back to Main Menu")
        choice = input(Fore.CYAN + "\n Select option (1-8): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-8.")
            continue
        if choice == 1:
            income_budget.input_income(data)
            save_data(data)
        elif choice == 2:
            income_budget.remove_income(data)
            save_data(data)
        elif choice == 3:
            income_budget.update_income(data)
            save_data(data)
        elif choice == 4:
            income_budget.input_budget(data)
            save_data(data)
        elif choice == 5:
            income_budget.remove_budget(data)
            save_data(data)
        elif choice == 6:
            income_budget.update_budget(data)
            save_data(data)
        elif choice == 7:
            income_budget.total_income(data)
        elif choice == 8:
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-8.")

def expense_menu(data):
    os.system("clear")
    utils.show_title()
    while True:
        print(Fore.BLUE + "\n" + "="*50)
        print(Fore.CYAN + "           EXPENSE MENU")
        print(Fore.BLUE + "="*50)
        print(Fore.WHITE + "\n1. Add Expense        |   2. Remove Expense")
        print(Fore.WHITE + "3. Update Expense     |   4. Total Expenses")
        print(Fore.MAGENTA + "\n" + "-"*50)
        print(Fore.YELLOW + "5. Back to Main Menu")
        choice = input(Fore.CYAN + "\n Select option (1-5): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-5.")
            continue 
        if choice == 1:
            expense.input_expense(data)
            save_data(data)
        elif choice == 2:
            expense.remove_expense(data)
            save_data(data)
        elif choice == 3:
            expense.update_expense(data)
            save_data(data)
        elif choice == 4:
            expense.total_expense(data)
        elif choice == 5:
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-5.")

def calculator_menu():
    os.system("clear")
    utils.show_title()
    while True:
        print(Fore.YELLOW + "\n" + "="*50)
        print(Fore.CYAN + "           Calculators MENU")
        print(Fore.YELLOW + "="*50)
        print(Fore.WHITE + "\n1. Simple Investment Calculator")
        print(Fore.WHITE + "\n2. Compounding Calculator")
        print(Fore.MAGENTA + "\n" + "-"*50)
        print(Fore.YELLOW + "3. Back to Main Menu")
        choice = input(Fore.CYAN + "\n Select option (1-3): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-3.")
            continue
        if choice == 1:
            calculator.investment_calc()
        elif choice == 2:
            calculator.compounding_calc()
        elif choice == 3:
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-3.")
        
def savings_menu(data):
    os.system("clear")
    utils.show_title()
    while True:
        print(Fore.MAGENTA + "\n" + "="*50)
        print(Fore.CYAN + "           SAVINGS MENU")
        print(Fore.MAGENTA + "="*50)
        print(Fore.WHITE + "\n1. Add Savings        |   2. Remove Savings")
        print(Fore.WHITE + "3. Update Savings     |   6. Total Savings")
        print(Fore.WHITE + "\n4. Set Savings Goal   |   5. Update Acquired Amount")
        print(Fore.BLUE + "\n" + "-"*50)
        print(Fore.YELLOW + "7. Back to Main Menu")
        choice = input(Fore.CYAN + "\n Select option (1-7): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-7.")
            continue
        if choice == 1:
            savings.add_savings(data)
            save_data(data)
        elif choice == 2:
            savings.remove_savings(data)
            save_data(data)
        elif choice == 3:
            savings.update_savings(data)
            save_data(data)
        elif choice == 4:
            savings.set_savings_goal(data)
            save_data(data)
        elif choice == 5:
            savings.update_goal(data)
            save_data(data)
        elif choice == 6:
            savings.total_savings(data)
        elif choice == 7:
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-7.")

def lent_borrowed_menu(data):
    os.system("clear")
    utils.show_title()
    while True:
        print(Fore.LIGHTGREEN_EX + "\n" + "="*50)
        print(Fore.CYAN + "       DEBT MENU")
        print(Fore.LIGHTGREEN_EX + "="*50)
        print(Fore.MAGENTA + "\n" + "~"*24 + " LENT " + "~"*24)
        print(Fore.WHITE + "1. Add Lent      |   2. Remove Lent")
        print(Fore.WHITE + "3. Update Lent   |   4. Total Lent")
        print(Fore.WHITE + "5. Lent History")
        print(Fore.MAGENTA + "\n" + "~"*22 + " BORROWED " + "~"*22)
        print(Fore.WHITE + "6. Add Borrowed    |   7. Remove Borrowed")
        print(Fore.WHITE + "8. Update Borrowed |   9. Total Borrowed")
        print(Fore.WHITE + "10. Borrowed History")
        print(Fore.BLUE + "\n" + "-"*50)
        print(Fore.YELLOW + "11. Back to Main Menu")
        choice = input(Fore.CYAN + "\n Select option (1-11): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-11.")
            continue
        if choice == 1:
            lent_borrowed.add_lent(data)
            save_data(data)
        elif choice == 2:
            lent_borrowed.remove_lent(data)
            save_data(data)
        elif choice == 3:
            lent_borrowed.update_lent(data)
            save_data(data)
        elif choice == 4:
            lent_borrowed.total_lent(data)
        elif choice == 5:
            lent_borrowed.lent_history(data)
        elif choice == 6:
            lent_borrowed.add_borrowed(data)
            save_data(data)
        elif choice == 7:
            lent_borrowed.remove_borrowed(data)
            save_data(data)
        elif choice == 8:
            lent_borrowed.update_borrowed(data)
            save_data(data)
        elif choice == 9:
            lent_borrowed.total_borrowed(data)
        elif choice == 10:
            lent_borrowed.borrowed_history(data)
        elif choice == 11:
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-11.")

def main():
    os.system("clear")
    utils.show_title()
    print(Fore.GREEN + "\n" + "☆"*50)
    print(Fore.YELLOW + "        WELCOME TO FIN-TRACK PLUS")
    print(Fore.GREEN + "☆"*50)  
    current_user = None
    while current_user is None:
        print(Fore.CYAN + "\n" + "-"*50)
        print(Fore.YELLOW + "           ACCOUNT ACCESS")
        print(Fore.CYAN + "-"*50)
        print(Fore.WHITE + "\n1. Sign In")
        print(Fore.WHITE + "2. Sign Up")
        print(Fore.MAGENTA + "\n" + "-"*50)
        choice = input(Fore.CYAN + " Press 1 to sign in or 2 to sign up: ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter 1 or 2.")
            continue
        if choice == 1:
            current_user = auth.auth_sign_in()
        elif choice == 2:
            if auth.auth_sign_up():
                continue  
            else:
                continue
        else:
            print(Fore.RED + "\n❌ Please choose 1 or 2")
        print()
    set_current_user(current_user)
    
    data = read_data(current_user["email"])
    
    while True:
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + "    SMART FINANCE TRACKER & ADVISOR")
        print(Fore.CYAN + "="*50)
        print(Fore.WHITE + "\n1. Income & Budget   |   2. Expenses")
        print(Fore.WHITE + "3. Savings           |   4. Debt")
        print(Fore.WHITE + "5. Financial Summary |   6. Calculators")
        print(Fore.WHITE + "7. Talk to Mark(AI Assistant)")
        print(Fore.MAGENTA + "\n" + "-"*50)
        print(Fore.RED + "8. Exit")
        choice = input(Fore.CYAN + "\n Select an option (1-8): ").strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print(Fore.RED + "\n❌ Invalid input! Please enter a number 1-8.")
            continue
        if choice == 1:
            income_budget_menu(data)
        elif choice == 2:
            expense_menu(data)
        elif choice == 3:
            savings_menu(data)
        elif choice == 4:
            lent_borrowed_menu(data)      
        elif choice == 5:
            summary.show_financial_summary(data)
        elif choice == 6:
             calculator_menu()
        elif choice == 7:
            recommendations.talk_to_mark()
        elif choice == 8:
            print(Fore.RED + "\n" + "♥ "*25)
            print(Fore.YELLOW + "   Thank you for using FIN-TRACK PLUS!")
            print(Fore.RED + "♥ "*25 + "\n")
            save_data(data)
            break
        else:
            print(Fore.RED + "\n❌ Invalid selection! Please enter a number 1-8.")
if __name__ == "__main__":
    main()