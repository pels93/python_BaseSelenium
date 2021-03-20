import os
import sys
import time


# in cmd
#        @tags firefox edge chrome opera
# run_all_windows.py @nasa a b d f
print('Lauch the drivers:', str(sys.argv))


def start_old(tags: str,browser: str):
    os.system(
        '(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "' + browser + '",&echo "enableDeleteOldReport": '
                                                                                   'false &echo })  > settings.json')
    os.system('start behave --tags '+tags+' --no-skipped --no-snippets')
    time.sleep(5)


if str(len(sys.argv[2]) > 0):
    start_old(str(sys.argv[1]),"firefox")
if str(len(sys.argv[3]) > 0):
    start_old(str(sys.argv[1]),"edge")
if str(len(sys.argv[4]) > 0):
    start_old(str(sys.argv[1]),"chrome")
if str(len(sys.argv[5]) > 0):
    start_old(str(sys.argv[1]),"opera")
