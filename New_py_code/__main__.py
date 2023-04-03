import pyautogui
from __funktion__ import *
import sys

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
file_path_config =  file_path + os.path.sep+ "cfg.ini"
file_path_Bilder = file_path +  os.path.sep+ "Bilder" + os.path.sep

file_path_Work_Folder = file_path + "/Work_Folder/"


new_py_name = pyautogui.prompt(text='What should the project be called?', title='New_py_Code' , default='')
default_folder = read_config( file_path_config, "default", "folder")
projekt_folder = pyautogui.prompt(text='what is the destination folder?', title='New_py_Code' , default=default_folder)
gituser_default = read_config( file_path_config, "default", "github_user")

projekt_folder = Folder_gen(new_py_name, projekt_folder )

py_name_folder = Folder_gen(new_py_name, projekt_folder )
readme_img_folder = Folder_gen("README_img", projekt_folder )
test_folder = Folder_gen("test", projekt_folder )

__funktion__temp = Read_File_Out(file_path + os.path.sep+ "__funktion__-temp.txt")
Create_File("__funktion__.py", py_name_folder, __funktion__temp)

__init__temp = Read_File_Out(file_path + os.path.sep+ "__init__-temp.txt")
Create_File("__init__.py", py_name_folder, __init__temp)

__main__temp = Read_File_Out(file_path + os.path.sep+ "__main__-temp.txt")
Create_File(f"{new_py_name}.py", py_name_folder, __main__temp)








