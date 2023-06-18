import abc

class Milk:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"Milk Type: {self.name}, Price: ${self.price}")


class MilkFlyweightFactory:
    milk_types = {}

    @staticmethod
    def get_milk_type(name, price):
        if name not in MilkFlyweightFactory.milk_types:
            milk_type = Milk(name, price)
            MilkFlyweightFactory.milk_types[name] = milk_type
        return MilkFlyweightFactory.milk_types[name]


def main():
    milk_list = [
        ("Full Cream", 2.5),
        ("Skimmed", 2.0),
        ("Soy", 3.0),
        ("Full Cream", 2.5)
    ]

    flyweight_factory = MilkFlyweightFactory()

    for milk_info in milk_list:
        name, price = milk_info
        milk_type = flyweight_factory.get_milk_type(name, price)
        milk_type.describe()


if __name__ == "__main__":
    main()
