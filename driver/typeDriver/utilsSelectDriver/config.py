import json
from driver.typeDriver.utilsSelectDriver.utilsSelectDriver import *

settings = None


def load_settings():
    global settings
    with open(Utils.merge_directory_to_folder(Utils.folder_proyect(), 'settings.json')) as f:
        settings = json.load(f)


load_settings()
