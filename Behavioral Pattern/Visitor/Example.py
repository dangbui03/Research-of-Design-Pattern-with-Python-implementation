import abc

class Building(metaclass=abc.ABCMeta):
    """
    The abstract base class that defines the accept method for accepting a visitor.
    """
    @abc.abstractmethod
    def accept(self, visitor):
        pass

class ResidentialBuilding(Building):
    """
    A concrete class representing a residential building.
    """
    def accept(self, visitor):
        visitor.visit_residential_building(self)

class Bank(Building):
    """
    A concrete class representing a bank building.
    """
    def accept(self, visitor):
        visitor.visit_bank(self)

class CoffeeShop(Building):
    """
    A concrete class representing a coffee shop building.
    """
    def accept(self, visitor):
        visitor.visit_coffee_shop(self)

class InsuranceAgent:
    """
    The visitor class representing an insurance agent.
    """
    def visit_residential_building(self, building):
        print("Selling medical insurance to the residents.")

    def visit_bank(self, building):
        print("Selling theft insurance to the bank.")

    def visit_coffee_shop(self, building):
        print("Selling fire and flood insurance to the coffee shop.")


def main():
    residential_building = ResidentialBuilding()
    bank = Bank()
    coffee_shop = CoffeeShop()

    insurance_agent = InsuranceAgent()

    residential_building.accept(insurance_agent)
    bank.accept(insurance_agent)
    coffee_shop.accept(insurance_agent)


if __name__ == "__main__":
    main()
