import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import screenshot_path

@pytest.mark.parametrize("row_index", [0, 1, 2, 3])
def test_login_matrix(page, load_csv, row_index):
    rows = load_csv("data/users.csv")
    row = rows[row_index]
    print(row)
    login = LoginPage(page)
    inventory = InventoryPage(page)

    try:
        login.open()
        login.login(row["user"], row["pwd"])
        expected_ok = row["ok"].lower() == "true"
        if expected_ok:
            assert inventory.is_loaded(), "Debería entrar al inventario"
        else:
            assert login.has_error(), "Debería mostrar error"
    except Exception:
        page.screenshot(path=screenshot_path(f"login_{row_index}_fail"))
        raise
