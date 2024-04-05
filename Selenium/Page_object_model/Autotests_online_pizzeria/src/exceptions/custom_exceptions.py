class CheckoutError(Exception):
    """Exception raised for errors during the checkout process."""

    def __init__(self, message="Error during checkout"):
        self.message = message
        super().__init__(self.message)
