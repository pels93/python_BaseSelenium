class mobile_page():
    def __init__(self,appium):
        self.appium=appium
    
    def popup(self):
          self.appium.utilsDriver.wait(2)
          self.el1 = self.appium.UtilsMobileElements.find_elements_by_id("consent_dialog_no_button")
    
    def findElements(self):
        self.punto = self.appium.UtilsMobileElements.find_element_by_id_or_xpath("period",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[25]")
        self.delete = self.appium.UtilsMobileElements.find_elements_by_id("backspace")
        self.num0 = self.appium.UtilsMobileElements.find_element_by_id("n0")
        self.num1 = self.appium.UtilsMobileElements.find_element_by_id("n1")
        self.num2 = self.appium.UtilsMobileElements.find_element_by_id("n2")
        self.num3 = self.appium.UtilsMobileElements.find_element_by_id("n3")
        self.num4 = self.appium.UtilsMobileElements.find_element_by_id("n4")
        self.num5 = self.appium.UtilsMobileElements.find_element_by_id("n5")
        self.num6 = self.appium.UtilsMobileElements.find_element_by_id("n6")
        self.num7 = self.appium.UtilsMobileElements.find_element_by_id("n7")
        self.num8 = self.appium.UtilsMobileElements.find_element_by_id("n8")
        self.num9 = self.appium.UtilsMobileElements.find_element_by_id("n9")
        self.suma = self.appium.UtilsMobileElements.find_element_by_id("add")
        self.resta = self.appium.UtilsMobileElements.find_element_by_id("subtract")
        self.division = self.appium.UtilsMobileElements.find_element_by_id("divide")
        self.multiplicacion = self.appium.UtilsMobileElements.find_element_by_id("multiply")
        self.igual = self.appium.UtilsMobileElements.find_element_by_id("equals")
        self.pantalla = self.appium.UtilsMobileElements.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.HorizontalScrollView[1]/android.widget.RelativeLayout/android.widget.RelativeLayout")
    
    def findResult(self): 
        #self.lista = self.appium.utilsMobileElements.findElementsByXPath("*//android.widget.ListView/android.widget.LinearLayout")
        self.result = self.appium.UtilsMobileElements.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
    
    def clear(self):
        self.C = self.appium.UtilsMobileElements.find_element_by_id("clear")
    
    def deletAll(self):
        self.AC = self.appium.UtilsMobileElements.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView[8]")

