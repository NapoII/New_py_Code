import pyautogui
from __funktion__ import *
import sys
from gen_readme import readme_gen


file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
file_path_config = file_path + os.path.sep + "cfg.ini"
file_path_Bilder = file_path + os.path.sep + "Bilder" + os.path.sep
Readme_top = file_path + os.path.sep + "Templates" + os.path.sep+"Readme_top.png"
file_path_Work_Folder = file_path + "/Work_Folder/"


new_py_name = pyautogui.prompt(text='What should the project be called?', title='New_py_Code', default='')
default_folder = read_config(file_path_config, "default", "folder")
projekt_folder = pyautogui.prompt(text='what is the destination folder?', title='New_py_Code', default=default_folder)
gituser_default = read_config(file_path_config, "readme", "github_user")

projekt_folder = Folder_gen(new_py_name, projekt_folder)

py_name_folder = Folder_gen(new_py_name, projekt_folder)
readme_img_folder = Folder_gen("README_img", projekt_folder)
test_folder = Folder_gen("test", projekt_folder)

__funktion__temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep+"__funktion__-temp.txt")
Create_File("__funktion__.py", py_name_folder, __funktion__temp)

__init__temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "__init__-temp.txt")
Create_File("__init__.py", py_name_folder, __init__temp)

__main__temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "__main__-temp.txt")
Create_File(f"{new_py_name}.py", py_name_folder, __main__temp)

gitignor = Read_File_Out(file_path + os.path.sep +"Templates" + os.path.sep + ".gitignor-temp.txt")
Create_File(f".gitignore", projekt_folder, __main__temp)

test_py_temp = Read_File_Out(file_path + os.path.sep + "Templates" + os.path.sep + "test_py-temp.txt")
Create_File(f"test.py", test_folder, test_py_temp)

readme_gen (new_py_name, projekt_folder, Readme_top, readme_img_folder, file_path_config )

setup_py_content = f"""from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='{new_py_name}',
    version='0.1.0',    
    description=("!!! add short description !!!"),
    long_description = readme,
    long_description_content_type="text/markdown",
    url='https://github.com/{gituser_default}/{new_py_name}',
    author='{gituser_default}',
    author_email='!!! add mail !!!,
    license='MIT License',
    packages="!!! add content from requirements.txt !!!",
    install_requires= [],

    classifiers=[
    !!! add classifiers !!!
        ],)"""

Create_File(f"setup.py", projekt_folder, setup_py_content)
Create_File(f"requirements.txt", projekt_folder, "#add required py packages")
