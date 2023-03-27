####################################################################################################
# #   Intro

v = "0.0.1"
f0 = """                               

 %%%%%%%%%,                            ,######### 
 MMMMMMMMM:                            :MMMMMMMMM 
 MM#######,                            ,%%%%%%#MM 
 MM:                                          :MM 
 MM:      .,,,,  .,,,.                        :MM 
 MM:       .+%M+  .:..                        :MM 
 MM:        : %M+  :                          :MM 
 MM:        :  %M+ :   .,,:. ,::. .. ,:.      :MM 
 MM:        :   %M+:  .@: +#  %@. #% ,,       :MM 
 MM:        :    %M#  :M+,,:. .@%,:M,:        :MM 
 MM:        :     %@  .M:      :M: %@.        :MM 
 MM:       ,:,.    +   .:,,.    :  .:         :MM 
 MM:                                          :MM 
 MM:                                          :MM 
 MM:                                          :MM 
 MM:                                          :MM 
 MM:         ..                 .             :MM 
 MM:       :+,.,+:            ,#@             :MM 
 MM:      :M.   ,:             %@             :MM 
 MM:     .MM        .,,.    .,.%@   .,,       :MM 
 MM:     .M@       :#. %%  %+ .#@  +% :@.     :MM 
 MM:      @M     . M#  +M,:M:  %@ .M%,:+,     :MM 
 MM:      ,M,   ,% ##  +M.,M:  #@ .@%  ..     :MM 
 MM:       .+,,,:: .+,,+,  ,+,,%#, .+,,,      :MM 
 MM:                                          :MM 
 MM:                                    ......:MM 
 MMM@@@@@@,                            :MMMMMMMMM 
 MMMMMMMMM:                            :MMMMMMMMM 
 +++++++++.                            .::::::::: 
                                                  
                - New_py_Code
            - created by Napo_II
                  - """ + v + """
               - python 2.7
        - https://github.com/NapoII/

"""
print(" \nProgramm wird gestartet ...")

####################################################################################################
#import
import sys
import datetime
import os
import os, sys
import time
import pyautogui
import webbrowser
from pandas.io import clipboard
import shutil

################################################################################################################################

#def

def Folder_gen(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = "~/"+str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)

def Datei_name_mit_Zeit(FileName):
    Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
    FullName = (FileName+"-"+(Date))                           # Generiert Datei name
    return FullName

def Erstelle_TextDatei( Text_File_name, save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(Text_File_name)+".txt] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Erstelle_InI_Datei( save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\config.ini")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei [config.ini] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Fill_Datei(dir, toFill, Attribut):
    file1 = open(dir, Attribut)                                 # Datei wird geöffnet
    #print("Datei ["+str(dir) + "] wird beschrieben und gespeichtert...\n")
    file1.write(toFill)                                             # Datei wird gefüllt mit input
    file1.close()

def TimeStemp():
    TimeStemp = Date_Time=(time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp

def log(Log_input):
    Fill_Datei(Log_File, TimeStemp()+" --> " + Log_input+"\n", "a")
    print (TimeStemp()+" --> " + Log_input+"\n")

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def Erstelle_README_Datei( save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\README.md")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei [README.md] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def copy_image(source_file: str, dest_file: str) -> None:
    # Kopiert ein Bild von der Quell- zur Ziel-Datei.
    # `source_file` ist der Pfad zur Quelldatei, `dest_file` ist der Pfad zur Zieldatei.
    # Gibt nichts zurück.
    
    try:
        shutil.copy(source_file, dest_file)
    except IOError as e:
        print(f"Fehler beim Kopieren der Datei: {e}")
    else:
        print("Bild erfolgreich kopiert!")


################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"


Doku_Folder = Folder_gen ("New_py_Code", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/New_py_Code")
Log_File_name = Datei_name_mit_Zeit ("LogFile-New_py_Code")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0 + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")



################################################################################################################################
#def:
def Textdatei_copy_over(Text_File_name, save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    log("Textdatei ["+str(Text_File_name)+".txt] wird erstellt... [" +str(complete_Path_Text) + "]")
    file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
    #toFile = input("Write what you want into the field")                   # Datei input def.
    file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
    file1.close()
    return complete_Path_Text

def New_Folder(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   #full_path = os.path.expanduser(dir) 
   full_path = dir
   #                # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      log("Ordner Struktur existiert bereits")
      log("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      log ("Der Ordner [" + str(folder)+ "] wurde erstellt im Verzeichnis:\n   ->   " + str(full_path)+"\n") 
   return(full_path)

def New_py ( Name, dir, Inhalt):
    datei_name = str(Name)+".py"
    complete_Path = str(dir) + "//" + str(datei_name)     # Path + text datei name
    log("Textdatei ["+str(datei_name)+"] wird erstellt... [" +str(complete_Path) + "]")
    file1 = open(complete_Path, "w")                                         # Datei erstellen
    #toFile = input("Write what you want into the field")                   # Datei input def.
    file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
    file1.close()
    return complete_Path

################################################################################################################################
#Settings


Projekt_predir = pyautogui.prompt(text='Projekt Ziel Ordner festlegen.', title='Projekt Ziel Ordner (0/10)' , default='E:\\Pr0grame\\My_ Pyhton\\work_in_progress')
#Projekt_predir = pyautogui.prompt(text='Projekt Ziel Ordner festlegen.', title='Projekt Ziel Ordner (0/10)' , default='C:\\Users\\space\\Documents\\New_py_Code')
log ( "Projekt Ziel Ordner: [" +str(Projekt_predir) + "]\n")

New_name = pyautogui.prompt(text='Wie heißt das neue Projekt', title='Projekt Name (1/10)' , default='')
log ( "New Projekt Name: [" +str(New_name) + "]\n")
ASCII_Bild_confrim = pyautogui.confirm(text='Erstelle nun ein Logo für den Code.', title='ASCII_Bild erstellen. (3/10)', buttons=['Yes', "No"])
if ASCII_Bild_confrim == "Yes":
    ASCII_Bild_confrim = True
else:
    ASCII_Bild_confrim = False

if ASCII_Bild_confrim == True:
    webbrowser.open("https://asciiartattack.de/")
    log ( "https://asciiartattack.de/ gets Open.")

    ASCII_Bild = pyautogui.prompt(text='ASCII Bild einfügen', title='ASCII_Bild einfügen. (3/10)' , default='')
    log ( "ASCII_Bild:\n\n"+ str(ASCII_Bild) +"\n")

else:
    ASCII_Bild = """
                      ......                      
                   .::+++++++:,.                  
                 ,:+++++++++++++:.                
                :+++++++++++++++++.               
               ,++,,:++++++++++++++.              
              .++:   :+++++++++++++,              
              .++,   ,+++++++++++++,              
              .++:. .:+++++++++++++,              
              .+++::+++++++++++++++,              
              .++++++++++++++++++++,              
              .::::::::::++++++++++,              
                         :+++++++++,              
       ,:::::::::::::::::++++++++++,.:::::,.      
      :++++++++++++++++++++++++++++,.:::::::.     
     ,+++++++++++++++++++++++++++++,.::::::::.    
    .++++++++++++++++++++++++++++++,.::::::::,    
    ,++++++++++++++++++++++++++++++,.:::::::::    
    :++++++++++++++++++++++++++++++..:::::::::.   
   .++++++++++++++++++++++++++++++: ,:::::::::,   
   .++++++++++++++++++++++++++++++..::::::::::,   
   ,+++++++++++++++++++++++++++++..::::::::::::   
   ,++++++++++++++:::::::::::::,..:::::::::::::   
   ,++++++++++++:.            ..,::::::::::::::   
   ,+++++++++++, .,::::::::::::::::::::::::::::   
   ,++++++++++: ,:::::::::::::::::::::::::::::,   
   .++++++++++.,::::::::::::::::::::::::::::::,   
   .+++++++++: :::::::::::::::::::::::::::::::,   
    :++++++++:.:::::::::::::::::::::::::::::::.   
    ,++++++++:.:::::::::::::::::::::::::::::::    
    .++++++++:.::::::::::::::::::::::::::::::.    
     ,+++++++:.:::::::::::::::::::::::::::::,     
      ,++++++:.:::::::::::::::::::::::::::::.     
       .,::::,.::::::::::,,,,,,,,,,,,,,,,,.       
              .::::::::::.                        
              .::::::::::::::::::::,              
              .::::::::::::::::::::,              
              .:::::::::::::::,,:::,              
              .::::::::::::::.  .::,              
              .::::::::::::::    ::,              
               ::::::::::::::.  .::.              
               .::::::::::::::,,::,               
                ,::::::::::::::::,.               
                 .,:::::::::::::.                 
                   ..,,:::::,,.                   
                                                  """


################################################################################################################################
#Main Programm

Projekt_dir = New_Folder( New_name, Projekt_predir )
Work_Folder_dir = New_Folder( "Work_Folder", Projekt_dir )
Bilder_dir = New_Folder( "Bilder", Projekt_dir )
v = "0.0.1"
Main_py = New_py ( New_name, Projekt_dir, ( "py_name ="+" \"" +New_name + "\" \n"))
Fill_Datei(Main_py, ( "v = \"0.0.1\"\n"), "a")
Fill_Datei(Main_py, ( """####################################################################################################
# #   Intro

f0 = """), "a")
Fill_Datei(Main_py, ( " \"\"\" \n" +ASCII_Bild + "\n"), "a")
fill = open((file_path_Work_Folder +'Py_template.txt'), "r")
fill = (fill.read())
Fill_Datei(Main_py, fill, "a")

# #   Imports
Imports_py = New_py ( "Imports", Projekt_dir, "py_name = \"" + New_name +"\"" + "\nv = \"0.0.1\"\n")
fill_I = open((file_path_Work_Folder +'Imports_template.txt'), "r")
fill_I = (fill_I.read())
Fill_Datei(Imports_py, fill_I, "a")

# #   ini   
ini_dir = Erstelle_InI_Datei( Projekt_dir, "[Test]\n#Info\nTest = Test" )

Test_input_text = """\n#from Imports import*
#config_dir = file_path +"/config.ini"""

New_py ( "Test_1", Projekt_dir, """################################################################################################################################
#Test_1"""+str(Test_input_text))
New_py ( "Test_2", Projekt_dir, """################################################################################################################################
#Test_2"""+str(Test_input_text))
New_py ( "Test_3", Projekt_dir, """################################################################################################################################
#Test_3"""+str(Test_input_text))

README_true = pyautogui.confirm(text='Soll eine README.md erstellet werden?', title='add README.md', buttons=['Yes', 'No'])

# var
Full_readme_str =""
Git_owner = pyautogui.prompt(text='Git_owner', title='README.md' , default='NapoII')
repro_name = pyautogui.prompt(text='Name der Repro', title='README.md' , default=New_name)
discord_link = pyautogui.prompt(text='Discord link', title='README.md' , default="https://discord.gg/g7EW4P65")
discord_ID = pyautogui.prompt(text='Discord ID', title='README.md' , default="190307701169979393")
Description = pyautogui.prompt(text='Description von der Repro', title='README.md' , default="Coming soon...")
py_version = sys.version.split()[0]


# add Logo and top:

add_top_logo = f"""<p align="center">
<a href="https://github.com/{Git_owner}">
    <img src="Work_Folder\Readme_top.png"  alt=f"{Git_owner}">
</a>
</p>

"""

Full_readme_str += add_top_logo
Full_readme_str += f"""<center>

# {repro_name}
</center>
"""

# add badges:

add_badges= f"""
<p align="center">
<a href="https://github.com/{Git_owner}/{repro_name}/archive/refs/heads/main.zip">
    <img src="https://img.shields.io/github/downloads/{Git_owner}/{repro_name}/total" alt="downloads/total">
</a>

<a href="https://github.com/{Git_owner}/{repro_name}/archive/refs/heads/main.zip">
    <img src="https://img.shields.io/github/repo-size/{Git_owner}/{repro_name}" alt="github/repo-size">
</a>

<a href="https://github.com/{Git_owner}/{repro_name}/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/{Git_owner}/{repro_name}" alt="github/license">
</a>

<a href="https://github.com/{Git_owner}/{repro_name}/actions">
    <img src="https://img.shields.io/github/last-commit/{Git_owner}/{repro_name}" alt="github/last-commit">
</a>

<a href="https://github.com/{Git_owner}/{repro_name}/issues">
    <img src="https://img.shields.io/github/issues/{Git_owner}/{repro_name}?style=plastic" alt="github/issues">
</a>

<a href="https://github.com/{Git_owner}/{repro_name}/stargazers">
    <img src="https://img.shields.io/github/stars/{Git_owner}/{repro_name}?style=social" alt="github/stars">
</a>

<a href="{discord_link}">
    <img src="https://img.shields.io/discord/{discord_ID}?style=plastic" alt="discord">
</a>
</p>"""

Full_readme_str += add_badges

# add Description
#bash cmd
Full_readme_str += "\n\n"+ Description +"\n"
Full_readme_str += f"""## Running Locally

This application requires Python {py_version}.
```
git clone https://github.com/{Git_owner}/{repro_name}
pip install -r requirements.txt
run Code {repro_name}.py
```

## Example
coming soon...
"""

# Lizenz
current_year = datetime.datetime.now().year
year_string = str(current_year)
Full_readme_str += f"""## Lizenz

MIT License

Copyright (c) {year_string} {Git_owner}
<small><small><small>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
</small>
"""



if README_true == "Yes":
    print(Full_readme_str)
    Erstelle_README_Datei(Projekt_dir, Full_readme_str)

    copy_image(file_path_Work_Folder+"Readme_top.png", Work_Folder_dir)

print(f0)
pyautogui.alert(text=("""- New_py_Code
- created by Napo_II
- """ + v + """
- python 2.7
- https://github.com/NapoII/

["""+ str(Projekt_dir)+"""]
wird dem Clipboard hinzugefügt.
"""), title='New_py_Code', button='Done!')


webbrowser.open('file:///' + Projekt_dir)
clipboard.copy(Projekt_dir)
log("Das Projekt wurde erstellt und die Ordner adresse dem Clipboard hinzugefügt.")