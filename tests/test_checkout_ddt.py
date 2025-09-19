from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.helpers import screenshot_path
import time

def test_checkout_ddt(page, load_json, sqlite_conn):
    # Login válido fijo para el checkout
    login = LoginPage(page)
    inv = InventoryPage(page)
    cart = CartPage(page)
    chk  = CheckoutPage(page)

    try:
        login.open()
        login.login("standard_user", "secret_sauce")
        assert inv.is_loaded(), "No cargó inventario"
        time.sleep(2)

        # Productos desde JSON
        data = load_json("data/products.json")
        for slug in data["items"]:
            print(slug)
            inv.add_item(slug)
            time.sleep(2)

        inv.open_cart()
        time.sleep(2)
        cart.go_to_checkout()

        # Dirección desde SQLite
        cur = sqlite_conn.cursor()
        cur.execute("SELECT first, last, zip FROM addresses LIMIT 1")
        first, last, zipc = cur.fetchone()

        chk.fill_address(first, last, zipc)
        time.sleep(2)
        chk.finish_order()
        time.sleep(2)
        assert chk.success(), "No se completó la orden"
    except Exception:
        page.screenshot(path=screenshot_path("checkout_fail"))
        raise
