class TourStrategy:
    """
    The Strategy interface that defines the contract for tour strategies.
    """
    def plan_tour(self):
        pass

class WalkingTourStrategy(TourStrategy):
    """
    A concrete strategy that represents a walking tour.
    """
    def plan_tour(self):
        print("Planning a walking tour around Ho Chi Minh City.")
        # Logic for planning a walking tour

class BikingTourStrategy(TourStrategy):
    """
    A concrete strategy that represents a biking tour.
    """
    def plan_tour(self):
        print("Planning a biking tour around Ho Chi Minh City.")
        # Logic for planning a biking tour

class CarTourStrategy(TourStrategy):
    """
    A concrete strategy that represents a car tour.
    """
    def plan_tour(self):
        print("Planning a car tour around Ho Chi Minh City.")
        # Logic for planning a car tour

class HoChiMinhCityTour:
    """
    The Context class that holds a reference to the current tour strategy.
    """
    def __init__(self, tour_strategy):
        self.tour_strategy = tour_strategy

    def set_tour_strategy(self, tour_strategy):
        self.tour_strategy = tour_strategy

    def plan_tour(self):
        self.tour_strategy.plan_tour()

def main():
    # Create the tour strategies
    walking_tour_strategy = WalkingTourStrategy()
    biking_tour_strategy = BikingTourStrategy()
    car_tour_strategy = CarTourStrategy()

    # Create the Ho Chi Minh City tour with the default strategy
    hcm_city_tour = HoChiMinhCityTour(walking_tour_strategy)

    # Plan the tour using different strategies
    hcm_city_tour.plan_tour()

    hcm_city_tour.set_tour_strategy(biking_tour_strategy)
    hcm_city_tour.plan_tour()

    hcm_city_tour.set_tour_strategy(car_tour_strategy)
    hcm_city_tour.plan_tour()

if __name__ == "__main__":
    main()
