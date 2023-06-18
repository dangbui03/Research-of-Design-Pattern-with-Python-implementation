class ProductCatalog:
    """
    The ProductCatalog class represents the product catalog or inventory.
    """
    def __init__(self):
        self.products = {
            'iphone': 999,
            'macbook': 1999,
            'ipad': 799
        }

    def get_product_price(self, product):
        return self.products.get(product)

class ShoppingCart:
    """
    The ShoppingCart class represents the shopping cart.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

class PaymentGateway:
    """
    The PaymentGateway class represents the payment gateway.
    """
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        # Additional payment processing logic goes here

class OrderFacade:
    """
    The OrderFacade class provides a simplified interface for ordering products online through a phone.
    It hides the complexity of interacting with the catalog, shopping cart, and payment gateway.
    """
    def __init__(self):
        self.catalog = ProductCatalog()
        self.cart = ShoppingCart()
        self.payment_gateway = PaymentGateway()

    def add_to_cart(self, product):
        price = self.catalog.get_product_price(product)
        if price:
            item = Product(product, price)
            self.cart.add_item(item)
            print(f"Added {product} to the cart.")
        else:
            print(f"{product} is not available.")

    def remove_from_cart(self, product):
        item = next((item for item in self.cart.get_items() if item.get_name() == product), None)
        if item:
            self.cart.remove_item(item)
            print(f"Removed {product} from the cart.")
        else:
            print(f"{product} is not in the cart.")

    def checkout(self):
        total = self.cart.calculate_total()
        print(f"Total amount to be paid: ${total}")
        self.payment_gateway.process_payment(total)
        print("Order placed successfully!")

class Product:
    """
    The Product class represents a product.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

# Client code
def main():
    facade = OrderFacade()

    facade.add_to_cart('iphone')
    facade.add_to_cart('macbook')
    facade.remove_from_cart('macbook')
    facade.add_to_cart('ipad')

    facade.checkout()

if __name__ == "__main__":
    main()
