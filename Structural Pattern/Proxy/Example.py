import abc

class PaymentService(metaclass=abc.ABCMeta):
    """
    Define the interface for the payment service.
    """
    @abc.abstractmethod
    def pay(self, amount):
        pass

class RealPaymentService(PaymentService):
    """
    The actual implementation of the payment service.
    """
    def pay(self, amount):
        print(f"Paying ${amount}.")

class PaymentProxy(PaymentService):
    """
    The proxy class that controls access to the payment service.
    """
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def pay(self, amount):
        self._perform_additional_checks(amount)
        self.payment_service.pay(amount)
        self._log_payment(amount)

    def _perform_additional_checks(self, amount):
        # Perform additional checks or validations here
        print(f"Performing additional checks for payment of ${amount}.")

    def _log_payment(self, amount):
        # Log the payment details
        print(f"Payment of ${amount} logged successfully.")

def main():
    # Create an instance of the actual payment service
    real_payment_service = RealPaymentService()

    # Create a proxy for the payment service
    payment_proxy = PaymentProxy(real_payment_service)

    # Use the proxy to make a payment
    payment_proxy.pay(100)

if __name__ == "__main__":
    main()
