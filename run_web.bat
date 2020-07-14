@echo off
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "firefox"&echo }) > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "edge"&echo }) > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "chrome"&echo }) > settings.json
start behave --tags @nasa --no-skipped --no-snippets
ping -n 20 127.0.0.1 >nul
(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "opera"&echo }) > settings.json
start behave --tags @nasa --no-skipped --no-snippets