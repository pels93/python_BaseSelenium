import os
import sys

from behave import __main__ as behave_executable


def start_run_behave(tags: str = "~_Execute_All_"):
    if len(sys.argv) > 1:
        _run_bash_()
    else:
        behave_executable.main('--tags=' + tags + ' --no-skipped --no-snippets')


def _run_bash_():
    _create_outputlogs_()
    auxtags: str = str(sys.argv[2:]) \
        .replace("[", "") \
        .replace("]", "") \
        .replace("'", "") \
        .replace(",", "", 1)
    sys.stdout = open(os.path.join(ruta, str(sys.argv[1]) + ".txt"), 'w', encoding='utf-8')
    print(behave_executable.main('--tags=' + auxtags + ' --no-skipped --no-snippets'))
    sys.stdout.close()


def _create_outputlogs_():
    try:
        global ruta
        ruta =os.path.join(os.path.abspath(os.curdir),"output")
        if not os.path.isdir(ruta):
            os.mkdir(ruta)
        ruta = os.path.join(ruta, "logs")
        if not os.path.isdir(ruta):
            os.mkdir(ruta)
    except:
        pass


start_run_behave("@nasa")
