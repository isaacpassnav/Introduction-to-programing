#Initial empy list
shopping_cart = []
item_name = []
item_price = []

#Funtion to add an item to the cart
def add_item(item, price):
    shopping_cart.append(item)
    item_name.append(item)
    item_price.append(price)

#Funtion to display the list of product in the cart
def display_cart():
    if len(shopping_cart) == 0:
        print("The cart is empty")
    else:
        print("Products in the cart")
        for i, item in enumerate(shopping_cart):
            print( i+1, "-", item, "($"+ str(item_price[i])+ ")")

#Remove an item from the cart
def remove_item(index):
    if index >=1 and index <= len(shopping_cart):
        item =shopping_cart.pop(index-1)
        item_name.pop(index-1)
        item_price.pop(index-1)
        print(item, "has been remove from the cart ")
    else:
        print("Invalid index.   ")

#Calculate and display the total price
def total_price():
    if len(shopping_cart) == 0:
        print("The cart is empty.")
    else:
        total_price = sum(item_price)
        print("Total price: $", format (total_price, ".2f"))

#Main funtion 
def main ():
    while True:
        print("\n === Shopping cart ===")
        print("1. Add item")    
        print("2. Display cart")
        print("3. Remove item")
        print("4. Calculate total price")
        print("5. Quit")

        choice = input("Select an option:")

        if choice == "1":
            item = input("Enter the name: ")
            price = float(input("Enter the price of the item: "))
            add_item(item,price)
        elif choice == "2":
            display_cart ()
        elif choice == "3":
            index = int(input("Enter the index of the item to remove: "))
            remove_item(index)
        elif choice == "4":
            total_price ()
        elif choice == "5":
            print("Than you for to use our Shopping cart!")
            break
        else:
            print("Invalid option. Please enter again: ")

main()

        
