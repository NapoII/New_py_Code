import logNow
from logNow import log
import os
from configparser import ConfigParser


def read_config(config_dir, section, option):
    """Reads a specific option from a config file in a specific section.

    Args:
        config_dir (str): The path of the config file.
        section (str): The section where the searched option is located.
        option (str): The name of the option being searched for.

    Returns:
        str: The value of the searched option.
    """

    config = ConfigParser()
    config.read(config_dir)
    load_config = (config[section][option])

    print("Config loaded: [ "+(option) + " = " + (load_config)+" ]")

    return load_config


def Folder_gen(Folder_Name, Folder_dir):
    """Creates a new folder if it does not already exist.

           Args:
               folder_name (str): The name of the folder to be created.
               folder_dir (str): The directory in which the folder is to be created.

           Returns:
               str: The full path of the created folder.
    """

    print("Folder structure is checked and created if necessary...\n")
    folder = Folder_Name
    # Specifies desired file path
    #dir = "~/"+str(Folder_dir)+"/"+str(folder)
    full_path = Folder_dir + os.path.sep + Folder_Name
    # Adds file path with PC user name
    #full_path = os.path.expanduser(dir)
    # Checks file path for exsistance Ture/False
    if os.path.exists(full_path):
        print("Folder structure already exists")
        print("  ->   " + str(full_path))
    else:                                               # Creates folder if not available
        os.makedirs(full_path)
        log(f"The folder [{folder}] was created in the directory:\n  ->   {full_path}", "b")
        print("\n")
    return(os.path.normpath(full_path))


def Create_File(File_name, save_path, Inhalt):
    """Creates a new text file if it does not already exist and fills it with the specified content.

    Args:
        File_name (str): The name of the text file.
        save_path (str): The path where the text file should be saved.
        Content (str): The content to be written to the text file.

    Returns:
        str: The complete path of the created text file.

    """

    complete_Path_Text = save_path + os.path.sep + File_name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        # Create file
        file1 = open(complete_Path_Text, "w")
        # toFile = input("Write what you want into the field")                   # File input def.
        # File is filled with input
        file1.write(Inhalt)
        file1.close()
        log("\nfile ["+str(File_name)+"] is created...","b")
        return complete_Path_Text


def Read_File_Out(dir):
    """
    Reads the contents of a file located at the given directory path and returns it as a string.

    Args:
    dir (str): The directory path of the file to be read.

    Returns:
    content (str): The contents of the file as a string.
    """
    with open(dir, 'r') as f:
        content = f.read()

    return content
