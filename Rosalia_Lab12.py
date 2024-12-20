def display_menu():
    menu = {
        "Chicken": 130,
        "Rice": 10,
        "Burger": 60,
        "Water": 15
    }
    print("The Menu")
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")
    return menu

def select_item(menu):
    while True:
        choice = input("Enter your order: ")
        if choice in menu:
            return choice, menu[choice]
        print("Error. This item is not in the menu. Please try again.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input("Input Payment: "))
            if cash >= total_cost:
                return cash
            print(f"Not enough. The amount needed: ₱{total_cost:.2f}.")
        except ValueError:
            print("Error. Please enter a valid amount.")

def calculate_change(cash, total_cost):
    return cash - total_cost

def main():
    menu = display_menu()
    item, price = select_item(menu)
    print(f"You chose {item}, ₱{price:.2f}.")
    cash = process_payment(price)
    change = calculate_change(cash, price)
    print(f"Payment complete. Change: ₱{change:.2f}. Come again!")

if __name__ == "__main__":
    main()
