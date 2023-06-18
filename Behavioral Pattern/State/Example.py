import abc

class PhoneState(metaclass=abc.ABCMeta):
    """
    The State interface that defines the contract for different phone states.
    """
    @abc.abstractmethod
    def press_button(self):
        pass

class UnlockedState(PhoneState):
    """
    A concrete state representing the unlocked state of the phone.
    """
    def press_button(self):
        print("Executing various functions.")

class LockedState(PhoneState):
    """
    A concrete state representing the locked state of the phone.
    """
    def press_button(self):
        print("Showing unlock screen.")

class LowBatteryState(PhoneState):
    """
    A concrete state representing the low battery state of the phone.
    """
    def press_button(self):
        print("Showing charging screen.")

class Phone:
    """
    The Context class that holds a reference to the current state of the phone.
    """
    def __init__(self):
        self.current_state = UnlockedState()

    def set_state(self, state):
        self.current_state = state

    def press_button(self):
        self.current_state.press_button()

def main():
    phone = Phone()

    # Test with unlocked state
    phone.press_button()

    # Change to locked state
    phone.set_state(LockedState())
    phone.press_button()

    # Change to low battery state
    phone.set_state(LowBatteryState())
    phone.press_button()

if __name__ == "__main__":
    main()
