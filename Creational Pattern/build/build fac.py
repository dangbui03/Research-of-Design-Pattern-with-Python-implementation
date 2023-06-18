from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.parts = {}

    def set_part(self, part, value):
        self.parts[part] = value

    def show(self):
        print("---------------------------")
        print("Vehicle Type: {}".format(self.vehicle_type))
        print(" Frame: {}".format(self.parts["frame"]))
        print(" Engine: {}".format(self.parts["engine"]))
        print(" #Wheels: {}".format(self.parts["wheels"]))
        print(" #Doors: {}".format(self.parts["doors"]))

class VehicleBuilder(ABC):
    def __init__(self):
        self.vehicle = Vehicle("")

    def get_vehicle(self):
        return self.vehicle

    def build_frame(self):
        pass

    def build_engine(self):
        pass

    def build_wheels(self):
        pass

    def build_doors(self):
        pass


class MotorCycleBuilder(VehicleBuilder):
    def __init__(self):
        super().__init__()

    def build_frame(self):
        self.vehicle.set_part("frame", "MotorCycle Frame")

    def build_engine(self):
        self.vehicle.set_part("engine", "500 cc")

    def build_wheels(self):
        self.vehicle.set_part("wheels", "2")

    def build_doors(self):
        self.vehicle.set_part("doors", "0")


class CarBuilder(VehicleBuilder):
    def __init__(self):
        super().__init__()

    def build_frame(self):
        self.vehicle.set_part("frame", "Car Frame")

    def build_engine(self):
        self.vehicle.set_part("engine", "2500 cc")

    def build_wheels(self):
        self.vehicle.set_part("wheels", "4")

    def build_doors(self):
        self.vehicle.set_part("doors", "4")


class ScooterBuilder(VehicleBuilder):
    def __init__(self):
        super().__init__()

    def build_frame(self):
        self.vehicle.set_part("frame", "Scooter Frame")

    def build_engine(self):
        self.vehicle.set_part("engine", "50 cc")

    def build_wheels(self):
        self.vehicle.set_part("wheels", "2")

    def build_doors(self):
        self.vehicle.set_part("doors", "0")


class Shop:
    def construct(self, vehicle_builder):
        vehicle_builder.build_frame()
        vehicle_builder.build_engine()
        vehicle_builder.build_wheels()
        vehicle_builder.build_doors()
        return vehicle_builder.get_vehicle()


def main():
    shop = Shop()

    builder = ScooterBuilder()
    scooter = shop.construct(builder)
    scooter.show()

    builder = CarBuilder()
    car = shop.construct(builder)
    car.show()

    builder = MotorCycleBuilder()
    motorcycle = shop.construct(builder)
    motorcycle.show()

if __name__ == "__main__":
    main()
