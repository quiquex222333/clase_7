class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first = "[data-test='firstName']"
        self.last  = "[data-test='lastName']"
        self.zip   = "[data-test='postalCode']"
        self.cont  = "[data-test='continue']"
        self.finish= "[data-test='finish']"
        self.ok    = ".complete-header"

    def fill_address(self, first, last, zipc):
        self.page.fill(self.first, first)
        self.page.fill(self.last, last)
        self.page.fill(self.zip, zipc)
        self.page.click(self.cont)

    def finish_order(self):
        self.page.click(self.finish)

    def success(self) -> bool:
        return self.page.locator(self.ok).inner_text().strip().lower().startswith("thank you")
