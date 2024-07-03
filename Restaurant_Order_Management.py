#You have been tasked with developing an order management system for a busy restaurant to streamline the ordering process and improve customer satisfaction. 
#The restaurant receives orders for food and drinks from customers, and the orders need to be processed and delivered efficiently. 
# Your objective is to design and implement a system that uses a queue to address each of the orders, in order that they were placed.
#Task 1

#Create an "Order" class which should include:
#- a list of meals ordered
#- table number
#- next


class Order():
    def __init__(self, meals, table_number):
        self.meals = meals
        self.table_number = table_number
        self.next = None

#Task 2

#Create a "Kitchen" class which should include the following methods:
#add_order() - adds order to kitchen queue
#cook_order() - removes order from the queue
#delete_order(table) - removes a tables order from the queue 
#view_orders() - should print out all the orders (Get creative with this, perhaps printing the table number followed by the meal(s))

class Kitchen():
    def __init__(self):
        self.orders = None

    def add_order(self, order): #O(n)
        if self.orders is None:
            self.orders = order
        else:
            current = self.orders
            while current.next is not None:
                current = current.next
            current.next = order
    
    def cook_order(self): #O(1)
        if self.orders is None: 
            print("No orders in queue")
            return
        else:
            print(f"Cooking order for table {self.orders.table_number} with meals: {', '.join(self.orders.meals)}") 
            self.orders = self.orders.next
    
    def delete_order(self, table): #O(n)
        if self.orders is None:
            print("No orders in queue")
            return
        elif self.orders.table_number == table: 
            self.orders = self.orders.next
        else:
            current = self.orders
            while current.next is not None and current.next.table_number != table:
                current = current.next
            if current.next is not None:
                current.next = current.next.next
    
    def view_orders(self): #O(n)
        if self.orders is None:
            print("No orders in queue")
            return
        else:
            current = self.orders
            while current is not None:
                print(f"Table {current.table_number}: {', '.join(current.meals)}")
                current = current.next
    

# Testing the Kitchen class
kitchen = Kitchen()

# Adding orders to the kitchen queue

order1 = Order(['Burger', 'Fries'], 1)
order2 = Order(['Pasta', 'Salad'], 2)
order3 = Order(['Steak', 'Soda'], 3)

kitchen.add_order(order1)

kitchen.add_order(order2)

kitchen.add_order(order3)

# Viewing all orders

kitchen.view_orders()

# Cooking an order

kitchen.cook_order()

# Viewing remaining orders

kitchen.view_orders()

# Deleting an order

kitchen.delete_order(2)




