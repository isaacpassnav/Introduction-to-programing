
# Brother Isaac Pasapera
# Initial empty list of products
shopping_cart = []
item_names = []
item_prices = []

# Function to add an item to the cart
def add_item(item, price):
    shopping_cart.append(item)
    item_names.append(item)
    item_prices.append(price)
    print(item, "has been added to the cart!") 
# Function to display the list of products in the cart
def display_cart():
    if len(shopping_cart) == 0:
        print("The cart is empty.")
    else:
        print("Products in the cart:")
        for i, item in enumerate(shopping_cart):
            print(i+1, "-", item, "($"+str(item_prices[i])+")")

# Function to remove an item from the cart
def remove_item(index):
    if index >= 1 and index <= len(shopping_cart):
        item = shopping_cart.pop(index-1)
        item_names.pop(index-1)
        item_prices.pop(index-1)
        print(item, "has been removed from the cart.")
    else:
        print("Invalid index.")

# Function to calculate and display the total price
def calculate_total_price():
    if len(shopping_cart) == 0:
        print("The cart is empty.")
    else:
        total_price = sum(item_prices)
        print("Total price: $", format(total_price, '.2f'))

# Main program function
def main():
    while True:
        print("\n=== Shopping Cart ===")
        print("1. Add item")
        print("2. Display cart")
        print("3. Remove item")
        print("4. Calculate total price")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            item = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            add_item(item, price)
        elif choice == "2":
           display_cart()
        elif choice == "3":
            index = int(input("Enter the index of the item to remove: "))
            remove_item(index)
        elif choice == "4":
            calculate_total_price()
        elif choice == "5":
            print("Thank you for using the shopping cart!")
            break
        else:
            print("Invalid option. Please select again.")

# Execute the main program function
main()


