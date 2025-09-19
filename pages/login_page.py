from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user = "[data-test='username']"
        self.pwd  = "[data-test='password']"
        self.btn  = "[data-test='login-button']"
        self.err  = "[data-test='error']"

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(self.user, username)
        self.page.fill(self.pwd, password)
        self.page.click(self.btn)

    def has_error(self) -> bool:
        return self.page.locator(self.err).is_visible()
