from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
from selenium.webdriver.ie.options import Options


class internetExplorer():

    def start(self) -> WebDriver:
        return webdriver.Ie(executable_path=IEDriverManager().install(), options=self._option_())

    def _option_(self):
        opts: Options = Options()
        opts.ignore_protected_mode_settings = True
        opts.ignore_zoom_level = True
        opts.require_window_focus = True
        return opts
