class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Food(metaclass=Singleton):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def main():
    burger = Food("Burger")
    pizza = Food("Pizza")

    print(burger)  # Kết quả: Burger
    print(pizza)   # Kết quả: Pizza

    print(burger is pizza)  # Kết quả: True

if __name__ == "__main__":
    main()
