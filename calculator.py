import os
import utils
from colorama import Fore

def investment_calc():
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "        SIMPLE INVESTMENT CALCULATOR")
    print(Fore.CYAN + "="*50)
    try:
        print(Fore.BLUE + "\n" + "-"*50)
        initial_capital = float(input(Fore.WHITE + "💰 Enter your Investment Amount: "))
        expected_return = float(input(Fore.WHITE + "📈 Enter the expected annual return (%): "))
        time = float(input(Fore.WHITE + "⏰ Enter investment duration (years): "))
        print(Fore.BLUE + "-"*50)
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input. Please enter numbers only.")
        return
    profit = initial_capital * (expected_return/100) * time
    total_amount = profit + initial_capital
    print(Fore.GREEN + "\n" + "="*50)
    print(Fore.YELLOW + "         INVESTMENT Details")
    print(Fore.GREEN + "="*50)
    print(Fore.CYAN + f"   • Initial Capital: {Fore.WHITE}{initial_capital:,.2f}")
    print(Fore.CYAN + f"   • Expected Return: {Fore.WHITE}{expected_return}% per year")
    print(Fore.CYAN + f"   • Duration: {Fore.WHITE}{time} years")
    print(Fore.MAGENTA + f"\n💵 Profit Calculation:")
    print(Fore.CYAN + f"   • Total Profit: {Fore.WHITE}{profit:,.2f}")
    print(Fore.CYAN + f"   • Total Value: {Fore.WHITE}{total_amount:,.2f}")
    print(Fore.GREEN + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")

def compounding_calc():
    os.system("clear")
    utils.show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "       COMPOUNDING CALCULATOR")
    print(Fore.CYAN + "="*50)
    try:
        initial_capital = float(input(Fore.WHITE + "💰 Enter your Investment Amount: "))
        expected_return = float(input(Fore.WHITE + "📈 Enter the expected annual return (%): "))
        time = float(input(Fore.WHITE + "⏰ Enter investment duration (years): "))
        print(Fore.BLUE + "-"*50)
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input. Please enter numbers only.")
        return
    rate = expected_return / 100
    try:
        print(Fore.MAGENTA + "\n" + "-"*50)
        n = int(input(Fore.WHITE + "🔄 Compounding frequency per year\n   (12 = monthly, 4 = quarterly, 1 = yearly): "))
        if n <= 0:
            raise ValueError
        print(Fore.MAGENTA + "-"*50)
    except ValueError:
        print(Fore.RED + "\n❌ Invalid compounding frequency.")
        return
    lump_sum_value = initial_capital * (1 + rate / n) ** (n * time)
    print(Fore.BLUE + "\n" + "~"*50)
    while True:
        choice = input(Fore.WHITE + "Will you invest additional money monthly? (yes/no): ").strip().lower()
        if choice == "yes" or choice == "no":
            break
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")
    print(Fore.BLUE + "~"*50)
    sip = 0
    total_invested = initial_capital
    if choice == "yes":
        try:
            monthly_investment = float(input(Fore.WHITE + "\n💰 Enter monthly investment amount: "))
        except ValueError:
            print(Fore.RED + "\n❌ Invalid monthly investment amount.")
            return
        months = int(time * 12)
        monthly_rate = rate / 12
        sip = monthly_investment * ((1 + monthly_rate) ** months - 1) / monthly_rate
        total_invested += monthly_investment * months
    total_value = lump_sum_value + sip
    profit = total_value - total_invested
    print(Fore.GREEN + "\n" + "="*50)
    print(Fore.YELLOW + "        COMPOUND INVESTMENT Details")
    print(Fore.GREEN + "="*50)
    print(Fore.CYAN + f"   • Initial Capital: {Fore.WHITE}{initial_capital:,.2f}")
    print(Fore.CYAN + f"   • Expected Return: {Fore.WHITE}{expected_return}% per year")
    print(Fore.CYAN + f"   • Duration: {Fore.WHITE}{time} years")
    print(Fore.CYAN + f"   • Compounding: {Fore.WHITE}{n} times per year")
    if choice == "yes":
        print(Fore.CYAN + f"   • Monthly SIP: {Fore.WHITE}{monthly_investment:,.2f}")
    print(Fore.MAGENTA + f"\n💰 Total Investment: {Fore.WHITE}{total_invested:,.2f}")
    print(Fore.MAGENTA + f"📈 Total Profit: {Fore.WHITE}{profit:,.2f}")
    print(Fore.MAGENTA + f"💵 Total Value after {time} years: {Fore.WHITE}{total_value:,.2f}")
    print(Fore.GREEN + "="*50)
    input(Fore.BLUE + "\nPress Enter to go back... ")