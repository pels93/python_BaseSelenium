class google_Page():

    def __init__(self, seleium):
        self.selenium = seleium
        self.findElements()

    def findElements(self):
        self.barra = self.selenium.utilsWebElements.findElementByName("q")
    # self.btnStartSesion = self.selenium.utilsWebElements.findElementByCssSelector("a#gb_70.gb_pe.gb_4.gb_5c");
