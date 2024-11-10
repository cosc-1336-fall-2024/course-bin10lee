from dictionary import add_inventory,remove_inventory_widget

def menu():
    print("Main Menu/ 1.Add or Update Item/ 2.Delete Item/ 3.Exit")

def main():
    inventory={}
    while True:
        menu()
        choice=input("Enter your selection: ")

        if choice=='1':
            widget=input("Item name: ")
            quantity=int(input(" Quantity: "))
            add_inventory(inventory, widget, quantity)
            print(f"Inventory updated: {inventory}\n")

        elif choice=='2':
            widget=input("Enter item name to delete: ")
            remove_inventory_widget(inventory, widget)
            print(f"Inventory after delete: {inventory}\n")

        elif choice =='3':
            print("Exit")
            break
        else:
            print("Invalid value")
main()
