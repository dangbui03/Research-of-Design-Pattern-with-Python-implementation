class AirportMediator:
    """
    The Mediator class that coordinates communication between airplanes and the airport.
    """
    def __init__(self):
        self.airplanes = []

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    def request_landing(self, airplane):
        if self.check_runway_availability():
            print(f"Landing permission granted for {airplane}.")
            self.reserve_runway()
        else:
            print(f"Landing permission denied for {airplane}. Waiting for runway availability.")

    def runway_available(self):
        print("Runway is now available.")
        self.reserve_runway()

    def reserve_runway(self):
        print("Reserving the runway for landing.")

    def check_runway_availability(self):
        # Simulate runway availability
        return len(self.airplanes) == 0


class Airplane:
    """
    The Colleague class representing an airplane.
    """
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def request_landing(self):
        self.mediator.request_landing(self)

    def runway_available(self):
        print(f"{self.name}: Received notification that runway is available. Preparing for landing.")


def main():
    mediator = AirportMediator()

    airplane1 = Airplane("Airplane", mediator)
    airplane2 = Airplane("Helicopter", mediator)
    airplane3 = Airplane("Plane", mediator)

    mediator.register_airplane(airplane1)
    mediator.register_airplane(airplane2)
    mediator.register_airplane(airplane3)

    airplane1.request_landing()
    airplane2.request_landing()
    airplane3.request_landing()

    # Simulate runway becoming available
    mediator.runway_available()


if __name__ == "__main__":
    main()
