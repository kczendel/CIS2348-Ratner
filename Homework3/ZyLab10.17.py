# Kyle Dela Pena
# 2038252

class ItemToPurchase:
    # constructor
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # print item cost method
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $"
              + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    # input item 1
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # input item 2
    print()
    print("Item 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # print info
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity

    print()
    # total cost of each item
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    print()
    # total cost of both items
    print("Total: $" + str(total_cost))
