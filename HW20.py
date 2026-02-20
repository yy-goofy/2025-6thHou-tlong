#Name: Tristan long
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Item:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_cost(self):
        self.cost *= 2
    def take_stock_1_4th(self):
        self.stock *= 1/4

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Laptop = Item(32, 3947, 7)
Shirt = Item(164, 256, 2)
Phone = Item(80, 999, 1)

#3. Print the stock of all three objects and the cost of the second store item.
print("Laptop stock:", Laptop.stock)
print("Shirt stock:", Shirt.stock)
print("Phone stock:", Phone.stock)
print("Shirt cost:", Shirt.cost)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
Shirt.double_cost()
print("Shirt new cost:", Shirt.cost)

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
Phone.take_stock_1_4th()
print("Phone new stock:", Phone.stock)

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
try:
    print(Laptop.price)
except:
    print("Error the attribute does not exist.")
  
