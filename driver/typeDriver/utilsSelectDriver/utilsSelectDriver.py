from random import random
import shutil
import os
from os import path
from datetime import datetime

class Utils:

    @staticmethod
    def int_random(minimum, maximum):
        return int(minimum + (random() * (maximum - minimum)))

    @staticmethod
    def directory_user_pc():
        return os.path.expandvars("%userprofile%")

    @staticmethod
    def folder_delete(folder):
        shutil.rmtree(folder, ignore_errors=True)

    @staticmethod
    def folder_create(folder):
        enableDebug = False
        if not Utils.folder_exists(folder):
            try:
                os.mkdir(folder)
            except OSError:
                if enableDebug:
                    Utils.print_info(
                        "ERROR -> NOT created the directory \n"+folder)
            else:
                if enableDebug:
                    Utils.print_info(
                        "Successfully -> created the directory \n"+folder)

    @staticmethod
    def merge_directory_to_folder(directory, folder):
        return os.path.join(directory, folder)

    @staticmethod
    def folder_proyect():
        return os.path.abspath(os.curdir)

    @staticmethod
    def directory_file():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def folders_create_tree(ini, final):
        aux_ini = ini
        aux = str(final[len(aux_ini):])
        if path.exists(aux_ini):
            for x in range(aux.count('\\')):
                actualFolder = aux[aux.find('\\')+1:]
                if actualFolder.find('\\') > 0:
                    actualFolder = actualFolder[:actualFolder.find('\\')]
                aux_ini = Utils.merge_directory_to_folder(
                    aux_ini, Utils.folder_validate_name(actualFolder))
                aux = str(final[len(aux_ini):])
                Utils.folder_create(aux_ini)
            return aux_ini

    @staticmethod
    def folder_validate_name(name_folder):
        aux = name_folder
        if len(aux) > 80:
            aux = aux[0:50]
        if aux.find("\'") > 0:
            aux = aux.replace("\'", "")
        if aux.find("\"") > 0:
            aux = aux.replace("\"", "")
        if aux.find("@") > 0:
            aux = aux.replace("@", "")
        if aux.find(" ") > 0:
            aux = aux.replace(" ", "_")
        if aux.find(":") > 0:
            aux = aux.replace(":", "")
        if aux.find("/") > 0:
            aux = aux.replace("/", "")
        return aux.lstrip()

    @staticmethod
    def folder_exists(name_folder):
        return path.exists(name_folder)

    @staticmethod
    def get_date():
        now = datetime.now()
        return str(now.strftime("%Y%m%d%H%M%S"))

    @staticmethod
    def print_info(string):
        print("\n=================================")
        print(string)
        print("=================================")
