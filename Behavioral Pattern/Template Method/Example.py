import abc

class HouseConstructionTemplate(metaclass=abc.ABCMeta):
    """
    The abstract class that defines the template method for house construction.
    """
    def construct_house(self):
        self.lay_foundation()
        self.build_frame()
        self.build_walls()
        self.install_plumbing()
        self.install_electrical_wiring()
        self.finish_house()

    @abc.abstractmethod
    def lay_foundation(self):
        pass

    @abc.abstractmethod
    def build_frame(self):
        pass

    @abc.abstractmethod
    def build_walls(self):
        pass

    @abc.abstractmethod
    def install_plumbing(self):
        pass

    @abc.abstractmethod
    def install_electrical_wiring(self):
        pass

    def finish_house(self):
        print("Finishing the house.")


class StandardHouseConstruction(HouseConstructionTemplate):
    """
    A concrete class representing the construction of a standard house.
    """
    def lay_foundation(self):
        print("Laying the foundation for a standard house.")

    def build_frame(self):
        print("Building the frame of a standard house.")

    def build_walls(self):
        print("Building the walls of a standard house.")

    def install_plumbing(self):
        print("Installing plumbing for a standard house.")

    def install_electrical_wiring(self):
        print("Installing electrical wiring for a standard house.")


class CustomHouseConstruction(HouseConstructionTemplate):
    """
    A concrete class representing the construction of a custom house.
    """
    def lay_foundation(self):
        print("Laying the foundation for a custom house.")

    def build_frame(self):
        print("Building the frame of a custom house with specific modifications.")

    def build_walls(self):
        print("Building the walls of a custom house with specific modifications.")

    def install_plumbing(self):
        print("Installing plumbing for a custom house with specific requirements.")

    def install_electrical_wiring(self):
        print("Installing electrical wiring for a custom house with specific requirements.")


def main():
    standard_house = StandardHouseConstruction()
    standard_house.construct_house()

    print("---")

    custom_house = CustomHouseConstruction()
    custom_house.construct_house()


if __name__ == "__main__":
    main()
