import os
from colorama import Fore

# This function is for choosing different categories to add
def category_choice(categories, message):
    os.system("clear")
    show_title()
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "           SELECT CATEGORY")
    print(Fore.CYAN + "="*50) 
    print(Fore.MAGENTA + "\n📋 Choose one of the following categories:")
    for index, category in enumerate(categories, 1):
        print(Fore.CYAN + f"   {index}. {Fore.WHITE}{category.capitalize()}")   
    print(Fore.BLUE + "\n💡 Type 'done' when you want to finish.")
    print(Fore.CYAN + "="*50)
    while True:
        print(Fore.BLUE + "\n" + "-"*50)
        choice = input(Fore.WHITE + f"👉 {message}").strip().lower()
        if choice == "done":
            return "done"
        if choice.isdigit():
            index = int(choice)
            if index >= 1 and index <= len(categories):
                selected = categories[index - 1]
                print(Fore.GREEN + f"\n✅ Selected: {selected.capitalize()}")
                print(Fore.BLUE + "-"*50)
                return selected
            else:
                print(Fore.RED + f"\n❌ Invalid number! Please choose 1-{len(categories)}.")
        elif choice in categories:
            print(Fore.GREEN + f"\n✅ Selected: {choice.capitalize()}")
            print(Fore.BLUE + "-"*50)
            return choice
        else:
            print(Fore.RED + f"\n❌ Invalid choice! Please enter a number (1-{len(categories)}) or type 'done'.")

# This function is for removing an item from the file
def remove_items(data, name):
    os.system("clear")
    show_title()
    if data == []:
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + "           REMOVE ITEMS")
        print(Fore.CYAN + "="*50)
        print(Fore.YELLOW + "\n📭 You have nothing to remove.")
        print(Fore.CYAN + "="*50)
        return
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + f"           REMOVE {name.upper()}S")
    print(Fore.CYAN + "="*50)   
    while True:
        print(Fore.MAGENTA + f"\n📋 Current {name}s ({len(data)} items):")
        for index, item in enumerate(data, 1):
            value = item.get("Amount", item.get("Budget", ""))
            print(Fore.CYAN + f"   {index}. {item[name]} - {Fore.WHITE}{value:.2f}")
        print(Fore.BLUE + "\n💡 Enter the number or name to remove.")
        print(Fore.BLUE + "💡 Type 'done' to finish.")
        print(Fore.BLUE + "-"*50)       
        choice = input(Fore.WHITE + f"👉 Enter the {name} you want to remove: ").strip().lower()
        if choice == "done":
            break
        if choice.isdigit():
            index = int(choice)
            if index >= 1 and index <= len(data):
                removed_item = data[index - 1]
                data.pop(index - 1)
                print(Fore.GREEN + f"\n✅ Removed: {removed_item[name].capitalize()} - {removed_item.get('Amount', removed_item.get('Budget', '')):.2f}")
            else:
                print(Fore.RED + f"\n❌ Invalid number! Please choose 1-{len(data)}.")
            continue
        removed = False
        for item in data:
            if str(item[name]).lower() == choice:
                data.remove(item)
                removed = True
                print(Fore.GREEN + f"\n✅ Removed: {item[name].capitalize()} - {item.get('Amount', item.get('Budget', '')):.2f}")
                break
        if not removed:
            print(Fore.RED + f"\n❌ No item found with that {name.lower()}. Please try again.")

# This function is for updating a value of an item from the file
def update_items(data, name):
    os.system("clear")
    show_title()
    if data == []:
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + f"           UPDATE {name.upper()}S")
        print(Fore.CYAN + "="*50)
        print(Fore.YELLOW + "\n📭 You have nothing to update.")
        print(Fore.CYAN + "="*50)
        return
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + f"           UPDATE {name.upper()}S")
    print(Fore.CYAN + "="*50) 
    while True:
        print(Fore.MAGENTA + f"\n📋 Current {name}s ({len(data)} items):")    
        for index, item in enumerate(data, 1):
            value = item.get("Amount", item.get("Budget", ""))
            print(Fore.CYAN + f"   {index}. {item[name]} - {Fore.WHITE}{value:.2f}")
        print(Fore.BLUE + "\n💡 Enter the number or name to update.")
        print(Fore.BLUE + "💡 Type 'done' to finish.")
        print(Fore.BLUE + "-"*50)     
        choice = input(Fore.WHITE + f"👉 Enter the {name} you want to update: ").strip().lower()
        if choice == "done":
            break
        if choice.isdigit():
            index = int(choice)
            if index >= 1 and index <= len(data):
                item = data[index - 1]
                current_value = item.get("Amount", item.get("Budget", ""))
                print(Fore.CYAN + f"\n📌 Selected: {item[name].capitalize()}")
                print(Fore.CYAN + f"💵 Current Value: {Fore.WHITE}{current_value:.2f}")
                print(Fore.BLUE + "-"*50)       
                try:
                    new_value = float(input(Fore.WHITE + "💰 Enter the new value: "))
                    if "Amount" in item:
                        item["Amount"] = new_value
                    else:
                        item["Budget"] = new_value
                    print(Fore.GREEN + f"\n✅ Updated {item[name].capitalize()} from {current_value:.2f} to {new_value:.2f}")
                except ValueError:
                    print(Fore.RED + "\n❌ Invalid value! Please enter a number.")
            else:
                print(Fore.RED + f"\n❌ Invalid number! Please choose 1-{len(data)}.")
            continue
        updated = False
        for item in data:
            if str(item[name]).lower() == choice:
                current_value = item.get("Amount", item.get("Budget", ""))
                print(Fore.CYAN + f"\n📌 Selected: {item[name].capitalize()}")
                print(Fore.CYAN + f"💵 Current Value: {Fore.WHITE}{current_value:.2f}")
                print(Fore.BLUE + "-"*50)     
                try:
                    new_value = float(input(Fore.WHITE + "💰 Enter the new value: "))
                    if "Amount" in item:
                        item["Amount"] = new_value
                    else:
                        item["Budget"] = new_value
                    print(Fore.GREEN + f"\n✅ Updated {item[name].capitalize()} from {current_value:.2f} to {new_value:.2f}")
                    updated = True
                except ValueError:
                    print(Fore.RED + "\n❌ Invalid value! Please enter a number.")
                break
        if not updated:
            print(Fore.RED + f"\n❌ No item found with that {name.lower()}. Please try again.")

def show_title():
    os.system("clear")
    print(Fore.GREEN + """
  ______ _____ _   _ _______ _____            _____ _  __  _____  _     _    _  _____ 
 |  ____|_   _| \ | |__   __|  __ \     /\   / ____| |/ / |  __ \| |   | |  | |/ ____|
 | |__    | | |  \| |  | |  | |__) |   /  \ | |    | ' /  | |__) | |   | |  | | (___  
 |  __|   | | | . ` |  | |  |  _  /   / /\ \| |    |  <   |  ___/| |   | |  | |\___ \ 
 | |     _| |_| |\  |  | |  | | \ \  / ____ \ |____| . \  | |    | |___| |__| |____) |
 |_|    |_____|_| \_|  |_|  |_|  \_\/_/    \_\_____|_|\_\ |_|    |______\____/|_____/ 
                                                                                      
                                                                                    
""")
    print(Fore.CYAN + "="*100)