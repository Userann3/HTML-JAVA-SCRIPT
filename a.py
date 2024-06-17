menu_items = {
    "Kadhai Chicken": {"Full": 465, "Half": 280},
    "Butter Chicken": {"Full": 450, "Half": 270},
    "Chicken Masala": {"Full": 500, "Half": 290},
    "Chicken Curry": {"Full": 440, "Half": 260},
    "Egg Curry": {"Full": 190, "Half": 100}
}

# Function to display the menu
def print_menu():
    print("Kadhai Chicken       Full     465/-       Half    280/-")
    print("Butter Chicken       Full     450/-       Half    270/-")
    print("Chicken Masala       Full     500/-       Half    290/-")
    print("Chicken Curry        Full     440/-       Half    260/-")
    print("Egg Curry            Full     190/-       Half    100/-")

# Function to get a valid menu item from the user
def get_valid_menu_item():
    while True:
        user_input = input("Enter the name of the dish you want to order: ").strip()
        if user_input in menu_items:
            return user_input
        else:
            print("Please enter a valid dish name from the menu.")

# Function to get the portion size (Full/Half) from the user
def get_valid_portion():
    while True:
        portion = input("Enter the portion size (Full/Half): ").strip().capitalize()
        if portion in ["Full", "Half"]:
            return portion
        else:
            print("Please enter 'Full' or 'Half'.")

# Function to get a valid quantity from the user
def get_valid_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to display the total bill
def print_bill(order):
    total = 0
    print("\n--- Bill ---")
    for item, details in order.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"{item} ({details['portion']}): {details['quantity']} x {details['price']}/- = {item_total}/-")
    print(f"Total Amount: {total}/-")

# Main program
def main():
    print_menu()
    order = {}
    
    while True:
        item = get_valid_menu_item()
        portion = get_valid_portion()
        quantity = get_valid_quantity()
        
        if item in order:
            order[item]['quantity'] += quantity
        else:
            order[item] = {
                'portion': portion,
                'price': menu_items[item][portion],
                'quantity': quantity
            }
        
        another = input("Do you want to order another item? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    
    print_bill(order)

if __name__ == "__main__":
    main()
