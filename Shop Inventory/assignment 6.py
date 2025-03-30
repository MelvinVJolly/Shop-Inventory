 #GROUP-6:Develop a Python application that tracks the inventory 
#of a shop using a dictionary, with product names as keys and stock quantities as values. 
#Implement features to add new products, remove products, update stock levels, and generate 
#a report of products that are low in stock (below a specified threshold).

# Initialize the inventory as an empty dictionary and set threshold value
inventory = {}
threshold = 25

def add_product(product_name, quantity):
    #Adds a new product or updates the quantity if it already exists
    if product_name in inventory:
        inventory[product_name] += quantity
    else:
        inventory[product_name] = quantity
    print(f"Added {quantity} of {product_name}.")

def remove_product(product_name):
    #Remove a product from the inventory
    if product_name in inventory:
        del inventory[product_name]
        print(f"Removed {product_name} from inventory.")
    else:
        print(f"{product_name} not found in inventory.")

def update_quantity(product_name, quantity):
    #Updates the quantity of an existing product
    if product_name in inventory:
        inventory[product_name] = quantity
        print(f"Updated {product_name} quantity to {quantity}.")
    else:
        print(f"{product_name} not found in inventory.")

def show_inventory():
    #Displays all products with their quantities
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")

def check_threshold():
    #Shows products with quantities below the threshold
    print(f"Products with quantity less than {threshold}:")
    for product, quantity in inventory.items():
        if quantity < threshold:
            print(f"{product}: {quantity}")

def menu():
    #Displays the menu and executes user choice
    while True:
        print("\n--- Shop Inventory Menu ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Show Inventory")
        print("5. Check Products Below Threshold")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            add_product(product_name, quantity)

        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            remove_product(product_name)

        elif choice == "3":
            product_name = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(product_name, quantity)

        elif choice == "4":
            show_inventory()

        elif choice == "5":
            check_threshold()

        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu function to start the program

if __name__ == "__main__":  # ✅ Fixed underscores
    menu()
