import collections.abc

class HoChiMinhCityTour(collections.abc.Iterable):
    """
    Implement the Iterator creation interface to return an instance of
    the proper ConcreteIterator.
    """
    def __init__(self):
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def __iter__(self):
        return HoChiMinhCityIterator(self.places)

class HoChiMinhCityIterator(collections.abc.Iterator):
    """
    Implement the Iterator interface.
    """
    def __init__(self, places):
        self.places = places
        self.current_index = 0

    def __next__(self):
        if self.current_index < len(self.places):
            place = self.places[self.current_index]
            self.current_index += 1
            return place
        else:
            raise StopIteration


def main():
    hcm_city_tour = HoChiMinhCityTour()
    hcm_city_tour.add_place("Ben Thanh Market")
    hcm_city_tour.add_place("War Remnants Museum")
    hcm_city_tour.add_place("Notre-Dame Cathedral Basilica of Saigon")
    hcm_city_tour.add_place("Cu Chi Tunnels")

    print("Exploring Ho Chi Minh City:")
    for place in hcm_city_tour:
        print(place)

if __name__ == "__main__":
    main()
