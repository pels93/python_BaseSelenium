@echo off
(echo {&echo "typeDriver": "appium",&echo "mobilePlatform":"android",&echo "urlServerAppium":"http://127.0.0.1:4723/wd/hub",&echo "mobileLanguage":"ES_es",&echo "app":"test.apk",&echo "nameMobile":"Pixel_2_API_27",&echo "versionMobile":"8.1.0",&echo "adbName":"emulator-5554"&echo }) > settings.json
adb kill-server
start %ANDROID_HOME%\tools\emulator.exe -avd Pixel_2_API_27 -no-snapshot -no-snapshot-load -no-snapshot-save -memory 512 -timezone Europe/Paris -no-boot-anim -no-audio -nocache
adb devices
adb devices
ping -n 30 127.0.0.1 >nul
behave --tags @mobile --no-skipped --no-snippets