class Player:
    """
    The Player class represents the game player whose state needs to be saved and restored.
    """
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def set_level(self, level):
        print(f"Setting {self.name}'s level to:", level)
        self.level = level

    def save_state(self):
        print(f"Saving {self.name}'s state.")
        return Memento(self.level)

    def restore_state(self, memento):
        self.level = memento.get_state()
        print(f"Restoring {self.name}'s level to:", self.level)

class Memento:
    """
    The Memento class stores the state of the Player.
    """
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

class Caretaker:
    """
    The Caretaker class manages the mementos of the Player.
    """
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

def main():
    player = Player("John", 1)
    caretaker = Caretaker()

    # Set initial level and save state
    player.set_level(2)
    caretaker.add_memento(player.save_state())

    # Increase level and save state
    player.set_level(3)
    caretaker.add_memento(player.save_state())

    # Decrease level
    player.set_level(2)

    # Restore to previous state
    memento = caretaker.get_memento(1)
    player.restore_state(memento)

if __name__ == "__main__":
    main()
