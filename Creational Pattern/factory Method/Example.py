import abc

class Animal(metaclass=abc.ABCMeta):
    """
    Define the interface for creating an animal object.
    """
    @abc.abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    """
    Implement the Animal interface for a Dog object.
    """
    def speak(self):
        return "Woof!"

class Cat(Animal):
    """
    Implement the Animal interface for a Cat object.
    """
    def speak(self):
        return "Meow!"

class AnimalCreator(metaclass=abc.ABCMeta):
    """
    Declare the factory method, which returns an object of type Animal.
    AnimalCreator may also define a default implementation of the factory
    method that returns a default Animal object.
    Call the factory method to create an Animal object.
    """
    def __init__(self):
        self.animal = self._create_animal()

    @abc.abstractmethod
    def _create_animal(self):
        pass

    def do_speak(self):
        return self.animal.speak()

class DogCreator(AnimalCreator):
    """
    Override the factory method to return an instance of a Dog.
    """
    def _create_animal(self):
        return Dog()

class CatCreator(AnimalCreator):
    """
    Override the factory method to return an instance of a Cat.
    """
    def _create_animal(self):
        return Cat()

def main():
    dog_creator = DogCreator()
    dog = dog_creator.do_speak()
    print(dog)  # Output: Woof!

    cat_creator = CatCreator()
    cat = cat_creator.do_speak()
    print(cat)  # Output: Meow!

if __name__ == "__main__":
    main()
