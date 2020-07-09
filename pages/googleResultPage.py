class google_result_search():

    def __init__(self, seleium):
        self.selenium = seleium
        self.findElements()

    def findElements(self):
        self.resultFirst = self.selenium.utilsWebElements.findElementByCssSelector(".r a")
