cart = {}

def show_menu():
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    
    if name in cart:
        cart[name]['quantity'] += quantity
    else:
        cart[name] = {'price': price, 'quantity': quantity}
    
    print(f"{name} added to cart.")

def remove_item():
    name = input("Enter item name to remove: ")
    
    if name in cart:
        del cart[name]
        print(f"{name} removed from cart.")
    else:
        print("Item not found in cart.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    
    print("\nMy Cart:")
    total = 0
    for item, details in cart.items():
        subtotal = details['price'] * details['quantity']
        total += subtotal
        print(f"{item} - ₱{details['price']} x {details['quantity']} = ₱{subtotal}")
    
    print(f"Total: ₱{total}")

def checkout():
    view_cart()
    print("Thank you for shopping!")
    cart.clear()

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
