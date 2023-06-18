import abc

class OrderCommand(metaclass=abc.ABCMeta):
    """
    The abstract base class for order commands.
    """
    @abc.abstractmethod
    def execute(self):
        pass

class TakeOrderCommand(OrderCommand):
    """
    A concrete command that represents taking an order.
    """
    def __init__(self, chef, order):
        self.chef = chef
        self.order = order

    def execute(self):
        self.chef.take_order(self.order)

class CookCommand(OrderCommand):
    """
    A concrete command that represents cooking a food item.
    """
    def __init__(self, chef, food_item):
        self.chef = chef
        self.food_item = food_item

    def execute(self):
        self.chef.cook(self.food_item)

class Chef:
    """
    The receiver class that executes the commands.
    """
    def take_order(self, order):
        print(f"Order taken: {order}")

    def cook(self, food_item):
        print(f"Cooking: {food_item}")

class Waiter:
    """
    The invoker class that triggers the commands.
    """
    def __init__(self):
        self.commands = []

    def place_order(self, command):
        self.commands.append(command)
        command.execute()

    def serve_orders(self):
        for command in self.commands:
            if isinstance(command, CookCommand):
                print("Serving the cooked food.")
            else:
                print("Order served.")
        self.commands = []

def main():
    chef = Chef()
    waiter = Waiter()

    # Take orders
    order1 = "Pizza"
    order2 = "Burger"
    take_order_command1 = TakeOrderCommand(chef, order1)
    take_order_command2 = TakeOrderCommand(chef, order2)
    waiter.place_order(take_order_command1)
    waiter.place_order(take_order_command2)

    # Cook food
    food_item1 = "Pizza"
    food_item2 = "Burger"
    cook_command1 = CookCommand(chef, food_item1)
    cook_command2 = CookCommand(chef, food_item2)
    waiter.place_order(cook_command1)
    waiter.place_order(cook_command2)

    # Serve orders
    waiter.serve_orders()

if __name__ == "__main__":
    main()
