class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.list = ".inventory_list"
        self.add_btn = "button[data-test^='add-to-cart-']"
        self.cart_icon = ".shopping_cart_link"

    def is_loaded(self):
        return self.page.locator(self.list).is_visible()

    def add_item(self, slug: str):
        locator = f"button[data-test='add-to-cart-{slug}']"
        print(locator)
        self.page.click(locator)

    def open_cart(self):
        self.page.click(self.cart_icon)
