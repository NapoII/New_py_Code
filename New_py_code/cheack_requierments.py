import ast
import builtins
import keyword
import sys
from sys import addaudithook
import pyautogui

from __funktion__ import *


def is_default_import(name):
    """
    Checks if a given string is a default Python import.
    """
    # Get a list of default Python imports
    default_imports = sys.modules.keys()

    # Check if the name is in the list of default imports
    if name in default_imports:
        return True
    
    return False


def extract_import_name(import_str):
    """
    Extracts the name of the module or package being imported from an import statement.
    """
    tree = ast.parse(import_str)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            return node.names[0].name
        elif isinstance(node, ast.ImportFrom):
            return node.module
    return None

    return import_name



def parse_string_by_line(input_string):
    """
    Parses a given string line by line and returns a list of the lines.
    """
    lines = input_string.strip().split("\n")
    return lines

requirements = pyautogui.prompt(text='imputt the ctx from the requirements ', title='requirements' , default='')
requirements = parse_string_by_line(requirements)

import_list_len = len(requirements)
new_requirements = []

while True:
    import_list_len = len(requirements)
    if import_list_len == 0:
        break

    item = requirements.pop()
    print(item)
    item = extract_import_name(item)
    print(item)
    x = is_default_import(item)
    print (item)
    if x == True:
        new_requirements.insert(0,item)
    print(f"{x}\n")

print(new_requirements)



