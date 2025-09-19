import csv, json, sqlite3, pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    ctx = browser.new_context()
    page = ctx.new_page()
    yield page
    ctx.close()

@pytest.fixture(scope="session")
def load_csv():
    def _load(path):
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    return _load

@pytest.fixture(scope="session")
def load_json():
    def _load(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return _load

@pytest.fixture(scope="session")
def sqlite_conn():
    conn = sqlite3.connect("data/testdata.db")
    yield conn
    conn.close()
