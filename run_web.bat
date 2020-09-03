@echo off
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "firefox",&echo "enableDeleteOldReport": true &echo })  > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "edge",&echo "enableDeleteOldReport": true &echo })  > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "chrome",&echo "enableDeleteOldReport": true &echo })  > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "opera",&echo "enableDeleteOldReport": true &echo })  > settings.json
start behave --tags @nasa --no-skipped --no-snippets