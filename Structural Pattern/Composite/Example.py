import abc

class Component(metaclass=abc.ABCMeta):
    """
    Định nghĩa giao diện chung cho các thành phần trong cấu trúc composite.
    """
    @abc.abstractmethod
    def buy(self):
        pass

class Product(Component):
    """
    Đại diện cho một sản phẩm cụ thể trong siêu thị.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def buy(self):
        print(f"Purchased product: {self.name}, Price: {self.price}")

class Category(Component):
    """
    Đại diện cho một danh mục sản phẩm trong siêu thị. Bao gồm nhiều sản phẩm hoặc danh mục con khác.
    """
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def buy(self):
        print(f"Purchased category: {self.name}")
        for child in self.children:
            child.buy()

def main():
    # Tạo các sản phẩm
    product_1 = Product("Milk", 2.5)
    product_2 = Product("Bread", 1.0)
    product_3 = Product("Eggs", 3.0)

    # Tạo danh mục sản phẩm nước uống
    drinks_category = Category("Drinks")
    drinks_category.add(product_1)
    drinks_category.add(product_2)

    # Tạo danh mục sản phẩm thực phẩm
    groceries_category = Category("Groceries")
    groceries_category.add(drinks_category)
    groceries_category.add(product_3)

    # Mua hàng
    groceries_category.buy()

if __name__ == "__main__":
    main()
