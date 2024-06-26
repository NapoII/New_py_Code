import os
import sys
import webbrowser

import pyautogui
from util.__funktion__ import *
from util.gen_readme import readme_gen
from pandas.io import clipboard

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
file_path_config = file_path + os.path.sep + "config"+ os.path.sep +"config.ini"
file_path_Bilder = file_path + os.path.sep + "Bilder" + os.path.sep
Readme_top = file_path + os.path.sep + "Templates" + os.path.sep+"Readme_top.png"
font_path = file_path + os.path.sep + "Templates" + os.path.sep+"Rust.ttf"
LICENSE_path = file_path + os.path.sep + "Templates" + os.path.sep+"LICENSE"
file_path_Work_Folder = file_path + "/Work_Folder/"

new_py_name = pyautogui.prompt(text='What should the project be called?', title='New_py_Code', default='')
default_folder = read_config(file_path_config, "default", "folder")
projekt_folder = pyautogui.prompt(text='what is the destination folder?', title='New_py_Code', default=default_folder)
gituser_default = read_config(file_path_config, "readme", "github_user")

projekt_folder = Folder_gen(new_py_name, projekt_folder)

py_name_folder = Folder_gen(new_py_name, projekt_folder)
readme_img_folder = Folder_gen("README_img", projekt_folder)
test_folder = Folder_gen("test", projekt_folder)


util_folder = Folder_gen("util", py_name_folder)

full_doku_on_str = f'"""Full Doku on: https://github.com/{gituser_default}/{new_py_name}"'

__init__temp = full_doku_on_str
__init__temp += Read_File_Out(file_path + os.path.sep +"Templates" + os.path.sep + "__init__-temp.txt")
__init__temp += f" \"{gituser_default}\""
Create_File("__init__.py", util_folder, __init__temp)

__funktion__temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep+"__funktion__-temp.txt")
Create_File("__funktion__.py", util_folder, __funktion__temp)

config_folder = Folder_gen("config", py_name_folder)
config_temp = Read_File_Out(file_path + os.path.sep +
                         "Templates" + os.path.sep+"config_temp.txt")
Create_File("config.ini", config_folder, config_temp)


__main__temp = full_doku_on_str
__main__temp += Read_File_Out(file_path + os.path.sep +
                              "Templates" + os.path.sep + "__main__-temp.txt")
__main__temp += f"# {new_py_name}.py\nprint(f'Programme has been started!')\n"
Create_File(f"{new_py_name}.py", py_name_folder, __main__temp)

gitignor = f"/{new_py_name}.egg-info"
gitignor += Read_File_Out(file_path + os.path.sep +"Templates" + os.path.sep + ".gitignor-temp.txt")
Create_File(f".gitignore", projekt_folder, gitignor)

requirements_content = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "requirements-temp.txt")
Create_File(f"requirements.txt", projekt_folder, requirements_content)

add_license(LICENSE_path, projekt_folder)

TODO_md_txt_content = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "TODO_md.txt")
Create_File(f"TODO.md", projekt_folder, TODO_md_txt_content)

test_py_temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "test_py-temp.txt")
Create_File(f"test.py", test_folder, test_py_temp)

readme_gen(new_py_name, projekt_folder, Readme_top,readme_img_folder, file_path_config, font_path)

setup_py_content = f"""from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='{new_py_name}',
    version='0.1.0',    
    description="!!! add short description !!!",
    long_description = readme,
    long_description_content_type="text/markdown",
    url='https://github.com/{gituser_default}/{new_py_name}',
    author='{gituser_default}',
    author_email='!!! add mail !!!',
    license='MIT License',
    packages="!!! add content from requirements.txt !!!",
    install_requires= [],

    classifiers=[
    !!! add classifiers !!!
        ],)"""

Create_File(f"setup.py", projekt_folder, setup_py_content)


webbrowser.open('file:///' + projekt_folder)
clipboard.copy(projekt_folder)
print("The project was created and the folder address was added to the clipboard..")
