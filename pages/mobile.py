class mobile_page():
    def __init__(self,appium):
        self.appium=appium
    
    def popup(self):
          self.appium.utilsDriver.wait(2)
          self.el1 = self.appium.utilsMobileElements.findElementsById("consent_dialog_no_button")
    
    def findElements(self):
        self.punto = self.appium.utilsMobileElements.findElementByIdOrXpath("period",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[25]")
        self.delete = self.appium.utilsMobileElements.findElementsById("backspace")
        self.num0 = self.appium.utilsMobileElements.findElementById("n0")
        self.num1 = self.appium.utilsMobileElements.findElementById("n1")
        self.num2 = self.appium.utilsMobileElements.findElementById("n2")
        self.num3 = self.appium.utilsMobileElements.findElementById("n3")
        self.num4 = self.appium.utilsMobileElements.findElementById("n4")
        self.num5 = self.appium.utilsMobileElements.findElementById("n5")
        self.num6 = self.appium.utilsMobileElements.findElementById("n6")
        self.num7 = self.appium.utilsMobileElements.findElementById("n7")
        self.num8 = self.appium.utilsMobileElements.findElementById("n8")
        self.num9 = self.appium.utilsMobileElements.findElementById("n9")
        self.suma = self.appium.utilsMobileElements.findElementById("add")
        self.resta = self.appium.utilsMobileElements.findElementById("subtract")
        self.division = self.appium.utilsMobileElements.findElementById("divide")
        self.multiplicacion = self.appium.utilsMobileElements.findElementById("multiply")
        self.igual = self.appium.utilsMobileElements.findElementById("equals")
        self.pantalla = self.appium.utilsMobileElements.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.RelativeLayout/android.widget.RelativeLayout")
    
    def findResult(self): 
        #self.lista = self.appium.utilsMobileElements.findElementsByXPath("*//android.widget.ListView/android.widget.LinearLayout")
        self.result = self.appium.utilsMobileElements.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
    
    def clear(self):
        self.C = self.appium.utilsMobileElements.findElementById("clear")
    
    def deletAll(self):
        self.AC = self.appium.utilsMobileElements.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[8]")

