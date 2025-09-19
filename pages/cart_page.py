class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_btn = "[data-test='checkout']"

    def go_to_checkout(self):
        self.page.click(self.checkout_btn)
