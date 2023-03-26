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
import os
import os, sys
import time
import pyautogui
import webbrowser
from pandas.io import clipboard

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
ASCII_Bild_confrim = pyautogui.confirm(text='Erstelle nun ein Logo für den Code.', title='ASCII_Bild erstellen. (3/10)', buttons=['Ja', "Nein"])
if ASCII_Bild_confrim == "Ja":
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