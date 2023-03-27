import pyautogui
import sys
import datetime
import os
import shutil

file_path = os.path.dirname(sys.argv[0])
file_path_ReadMe_output = file_path + "/ReadMe output/"
file_path_Work_Folder = file_path + "/Work_Folder/"
New_name ="Test"
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
    <img src="Readme_top.png"  alt=f"{Git_owner}">
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
    Erstelle_README_Datei(file_path_ReadMe_output, Full_readme_str)

    copy_image(file_path_Work_Folder+"Readme_top.png", file_path_ReadMe_output)