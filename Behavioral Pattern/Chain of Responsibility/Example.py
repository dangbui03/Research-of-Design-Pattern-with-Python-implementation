import abc

class DeliveryHandler(metaclass=abc.ABCMeta):
    """
    The abstract base class for delivery handlers.
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next_handler(self, handler):
        self.next_handler = handler

    @abc.abstractmethod
    def handle_delivery(self, package):
        pass

class DeliveryProcessor(DeliveryHandler):
    """
    A concrete delivery handler that processes the delivery request.
    """
    def handle_delivery(self, package):
        if package.is_fragile:
            print("Package is fragile. Applying special handling.")
            # Perform special handling for fragile packages
        else:
            print("Delivering the package.")

class DeliveryNotification(DeliveryHandler):
    """
    A concrete delivery handler that sends delivery notifications.
    """
    def handle_delivery(self, package):
        print("Sending delivery notification.")
        # Send delivery notification to the recipient

class DeliveryTracking(DeliveryHandler):
    """
    A concrete delivery handler that tracks the delivery progress.
    """
    def handle_delivery(self, package):
        print("Tracking the delivery progress.")
        # Track the package's delivery progress

def main():
    # Create the delivery handlers
    delivery_processor = DeliveryProcessor()
    delivery_notification = DeliveryNotification()
    delivery_tracking = DeliveryTracking()

    # Set up the chain of responsibility
    delivery_processor.set_next_handler(delivery_notification)
    delivery_notification.set_next_handler(delivery_tracking)

    # Simulate a delivery request
    package = Package(is_fragile=True)

    # Start the delivery process
    delivery_processor.handle_delivery(package)

class Package: #not affect the chain
    """
    Represents a package to be delivered.
    """
    def __init__(self, is_fragile=False):
        self.is_fragile = is_fragile

if __name__ == "__main__":
    main()
