import abc

# Abstraction
class Flower(metaclass=abc.ABCMeta):
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def display(self):
        pass

# Refined Abstraction
class Rose(Flower):
    def display(self):
        print(f"A beautiful rose with color {self.color}")

class Lily(Flower):
    def display(self):
        print(f"A lovely lily with color {self.color}")

# Implementor
class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply_color(self, flower):
        pass

# Concrete Implementor
class RedColor(Color):
    def apply_color(self, flower):
        print("Applying red color to the flower:")
        flower.display()

class BlueColor(Color):
    def apply_color(self, flower):
        print("Applying blue color to the flower:")
        flower.display()

def main():
    rose = Rose("Red")
    lily = Lily("White")

    red_color = RedColor()
    blue_color = BlueColor()

    red_color.apply_color(rose)
    blue_color.apply_color(rose)

    red_color.apply_color(lily)
    blue_color.apply_color(lily)

if __name__ == "__main__":
    main()
