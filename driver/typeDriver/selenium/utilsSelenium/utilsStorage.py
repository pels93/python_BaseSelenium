from selenium.webdriver.chrome.webdriver import WebDriver


class typeStorage:

    def __init__(self, driver, enableLocalStorage: bool):
        self.driver: WebDriver = driver
        if enableLocalStorage:
            self.type_sesion = "localStorage"
        else:
            self.type_sesion = "sessionStorage"

    def __len__(self):
        return self.driver.execute_script("return window." + self.type_sesion + ".length;")

    def all(self):
        return self.driver.execute_script("return window." + self.type_sesion + ";")

    def items(self):
        return self.driver.execute_script(
            "var ls = window." + self.type_sesion + ", items = {}; "
                                                    "for (var i = 0, k; i < ls.length; ++i) "
                                                    "  items[k = ls.key(i)] = ls.getItem(k); "
                                                    "return items; ")

    def keys(self):
        return self.driver.execute_script(
            "var ls = window." + self.type_sesion + ", keys = []; "
                                                    "for (var i = 0; i < ls.length; ++i) "
                                                    "  keys[i] = ls.key(i); "
                                                    "return keys; ")

    def get(self, key):
        return self.driver.execute_script("return window." + self.type_sesion + ".getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script("window." + self.type_sesion + ".setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script("window." + self.type_sesion + ".removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window." + self.type_sesion + ".clear();")

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()
