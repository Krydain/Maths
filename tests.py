# -*- coding: utf8 -*-

import os
import importlib

if __name__ == "__main__":
    root = os.getcwd()
    i = 0
    for file in os.listdir(root + "\Tests"):
        if file[-3:] == ".py" and file != "__init__.py":
            print("\n" if i != 0 else "Running the tests...\n")
            i = i + 1
            tmp = file[:-3]
            blob = importlib.import_module("Tests." + tmp)
            #print(dir(blob))
            print("|Liste des méthodes :", *((fct + "()") for fct in dir(blob) if fct[0] != "_"), sep='\n|- ')
    input("\n\nPress anykey to stop the program...")
