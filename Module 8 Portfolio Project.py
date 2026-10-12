class ItemToPurchase:
    def __init__(self):

        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")       
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []
    def add_item(self,item):
        self.cart_items.append(item)
    def remove_item(self,name):
        found = False
        for item in self.cart_items:
            if name == item.item_name:
                self.cart_items.remove(item)
                found = True
                break
        if found == False:
                print("Item not found in cart. Nothing removed.")
    def modify_item(self, item_to_modify):
            found = False
            for item in self.cart_items:
                if item.item_name == item_to_modify.item_name:
                    item.item_quantity = item_to_modify.item_quantity
                    found = True
                    break
            if found == False:
                print("Item not found in cart. Nothing modified.")
    def get_num_items(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity = total_quantity + item.item_quantity
        return total_quantity
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost = total_cost + (item.item_price * item.item_quantity)
        return total_cost
    def print_descriptions(self):
        for item in self.cart_items:
            item.print_item_description()
    def print_total(self):
        if len(self.cart_items) == 0:
           print("SHOPPING CART IS EMPTY")
        else:
           print("SHOPPING CART")
           print(f"Customer Name: {self.customer_name}")
           print(f"Today's Date: {self.current_date}")
           print(f"Number of Items: {self.get_num_items()}")
           for item in self.cart_items:
            item.print_item_cost()
           print(f"Total: ${self.get_cost_of_cart():.2f}")
def print_menu(cart):
    choice = ""
    while choice != "q":
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == "a":
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter item name: ")
            new_item.item_description = input("Enter item description: ")
            new_item.item_price = float(input("Enter item price: "))
            new_item.item_quantity = int(input("Enter item quantity: "))
            cart.add_item(new_item)
        elif choice == "r":
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == "c":
            name = input("Enter name of item to change: ")
            qty = int(input("Enter new quantity: "))
            changed = ItemToPurchase()
            changed.item_name = name
            changed.item_quantity = qty
            cart.modify_item(changed)
        elif choice == "i":
            cart.print_descriptions()
        elif choice == "o":
            cart.print_total()
        elif choice == "q":
            print("Goodbye")
        else:
            print("Invalid option. Please try again.")
name = input("Enter customer's name: ")
date = input("Enter today's date: ")
my_cart = ShoppingCart()
my_cart.customer_name = name
my_cart.current_date = date
print_menu(my_cart)
