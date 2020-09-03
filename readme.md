# BaseSelenium 

##### This project is designed in python to have a starter environment to test in selenium and appium.

## Support
	#NOTE this proyect only tested in Windows

Web  | Mobile
------------- | -------------
firefox  | Android
edge  | iOS
opera  |  
safari |  
google chrome  |  

## Requirement 
Python [Link](https://www.python.org/downloads/).

Android Studio [Link](https://developer.android.com/studio).

Appium Desktop [Link](http://appium.io/downloads.html).

When installed **Python**, run as Administrator
	
 
	install_depedence.bat


When run **Intellij** install the plugins `Cucumber for Java`, `Gherkin` and `Python Community Edition`


## Install
download the project and import it into Intellij.

### Sequence Run
                    
```seq
behave->aux_config.py: Read properties
aux_config.py->behave: Readed properties
behave->Features: init feature
Features->behave: inited feature
behave->StartTypeDriver.py: StartTypeDriver
StartTypeDriver.py->Selenium.py: Init browser type
Selenium.py->webdrivermanager: download browser driver type
Selenium.py->webdrivermanager: Init browser type
webdrivermanager->Selenium.py: Inited browser type
--------------------------------------------------------
Selenium.py->StartTypeDriver.java: 
Selenium.py->StartTypeDriver.java: Inited browser type
Selenium.py->StartTypeDriver.java: Inited browser type
-------------------------------------------------------
StartTypeDriver.java->Appium.java: Init mobile type
Appium.java->StartTypeDriver.java: Inited mobile type
behave->Features: Start test
Features->behave: End test
behave->StartTypeDriver.py: Close driver
StartTypeDriver.py->behave: Closed dirver
```

## Structure of the program
Directory  | Functionality
------------- | -------------
baseSelenium\features  | Contains the .features
baseSelenium\driver  | Contains the typeDriver Appium and Selenium
baseSelenium\pages   |  Contains the mapped elements
baseSelenium\features\steps  |  Contains the features steps
baseSelenium\driver\typeDriver\appium  | Contains the core of Appium
baseSelenium\driver\typeDriver\selenium   | Contains the core of Selenium


## Settings
The file `settings.json` is `baseSelenium`

setting file  `settings.json` from web
    
    {
	"typeDriver": "selenium",
    "typeBrowser": "chrome",
	"enableDeleteOldDrivers"=false
	"enableDeleteOldReport": true
	}

Setting file  `settings.json` from mobile

	{
	"typeDriver"="appium"
	"urlServerAppium"="http://127.0.0.1:4723/wd/hub"
	"mobilePlatform"="Android"
	"mobileLanguage"="ES_es"
	"app="test.apk"
	"nameMobile"="Pixel_2_API_27"
	"versionMobile"="8.1.0"
	"adbName"="emulator-5556"
	"enableDeleteOldReport": true
	}
     
----
## Write Steps
With **appium** you get the driver for context,it is advisable to make a global variable in the first step 
    
	# mod appium
    appium = None
    @Given('AppMobile Cerrar Popup')
    def startmobile(context):
        global appium
        appium = context.driver

With **selenium** you get the driver for context,it is advisable to make a global variable in the first step
 
 	# mod selenium
    selenium = None
    @Given('Encender el navegador')
    def startBrower(context):
        global selenium
        selenium = context.driver

## Run test

If you like run test in **behave**, open the terminal in the locate proyect and write

	run_web
	run_mobile

When the tests are complete, the ScreenShot will have been saved in the  `baseSelenium\ScreenShot`.

## Thank
>editor.md[Link](https://pandao.github.io/editor.md/en.html)



