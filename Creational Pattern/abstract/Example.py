from abc import ABC, abstractmethod
#abstract base product
class widget(ABC):
    def draw(self):
        pass

#concrete product family 1
class LinuxButton(widget):
    def draw(self):
        print("LinuxButton")

class LinuxMenu(widget):
    def draw(self):
        print("LinuxMenu")

#concrete product family 2
class WindowButton(widget):
    def draw(self):
        print("WindowButton")

class WindowMenu(widget):
    def draw(self):
        print("WindowMenu")

class Factory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_menu(self):
        pass

# Concrete factory for Linux
class LinuxFactory(Factory):
    def create_button(self):
        return LinuxButton()
    
    def create_menu(self):
        return LinuxMenu()

# Concrete factory for Windows    
class WindowsFactory(Factory):
    def create_button(self):
        return WindowButton()
    
    def create_menu(self):
        return WindowMenu()
    
class Client:
    
    def __init__(self, factory):
        self.factory = factory

    def draw(self):
        w = self.factory.create_button()
        w.draw()
        self.display_window_one()
        self.display_window_two()
        
    def display_window_one(self):
        w = [self.factory.create_button(), self.factory.create_menu()]
        w[0].draw()
        w[1].draw()

    def display_window_two(self):
        w = [self.factory.create_menu(), self.factory.create_button()]
        w[0].draw()
        w[1].draw()

# Main function
def main():
    factory = None

    # Switch between Linux and Windows factories
    platform = "LINUX"  # Change to "WINDOWS" for Windows factory
    if platform == "LINUX":
        factory = LinuxFactory()
    else:  # WINDOWS
        factory = WindowsFactory()

    client = Client(factory)
    client.draw()

if __name__ == "__main__":
    main()