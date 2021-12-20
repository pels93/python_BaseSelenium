import os
import sys
import threading
import platform
import time

init_tags: int = 0


def run_browsers(navegador:str, tags):
    auxtags: str = str(tags)\
        .replace("[", "")\
        .replace("]", "")\
        .replace("'", "")\
        .replace(",", "", 1)
    name_file: str = "behave_run.py"
    if navegador.lower() == "opera"\
            or navegador.lower() == "edge" \
            or navegador.lower() == "safari" \
            or navegador.lower() == "firefox" \
            or navegador.lower() == "chrome":
        os.system(
            '(echo {&echo "typeDriver": "selenium",&echo "typeBrowser": "' + navegador + '",&echo "enableDeleteOldReport": '
                                                                                         'false &echo })  > settings.json')
    aux = "python " + name_file + " " +navegador+" "+ (auxtags)
    if platform.system() == "Windows":  # Windows
        print(os.system('cmd /k "' + aux + '"'))
    elif platform.system() == "Darwin":  # Mac
        None
    elif platform.system() == "Linux":  # Linux
        os.system('cmd /k "' + aux + '"')

def run():
    global init_tags

    for x in range(len(sys.argv)):
        if str(sys.argv[x]).find("@") == 0 and init_tags == 0:
            init_tags = x

    for num_hilo in range(init_tags - 1):
        browser = threading.Thread(target=run_browsers, args=(sys.argv[num_hilo + 1], str(sys.argv[init_tags:])))
        browser.start()
        time.sleep(5)

run()

# python run_all.py chrome edge firefox opera @nasa --tags=@google
