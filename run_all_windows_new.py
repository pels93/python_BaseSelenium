import os
import sys
import threading
import platform

init_tags: int = 0


def run_browsers(navegador, tags):
    auxtags: str = str(tags).replace("[", "").replace("]", "").replace("'", "").replace(",", "",1)
    name_file: str = "behave_run.py"
    aux = "python " + name_file + " " + navegador + " " + (auxtags)
    print(aux)
    if platform.system() == "Windows":  # Windows
        None
        # os.system('cmd /k "' + aux + '"')
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


run()

# python run_all_windows_new.py chrome opera edge firefox @hola --tags=@perico,@android,@ola,@santander
