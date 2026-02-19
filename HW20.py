#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that init's self and 3 other attributes for store items (stock, cost, and weight).
class item:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_cost_10_percent(self):
        self.cost *= 10
    def take_stock_1_4th(self):
        self.stock *= 1/4

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.

Laptop = item(32, 3947,  7)
shirt = item(164, 256, 25)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"shirt stock:", shirt.stock)
print(f"Laptop cost:", Laptop.cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
Laptop.double_cost_10_percent()
print(Laptop.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
shirt.take_stock_1_4th()
print(shirt.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
try :
    Smartphone = item.weight(7)
    print(Smartphone.weight)
except :
    print("error")