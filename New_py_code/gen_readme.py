from __funktion__ import *
import pyautogui
import sys

def add_image_to_markdown(Alt_Text, path, link):
    """
    Returns a Markdown-formatted string that displays an image with a link.

    Parameters:
    - Alt_Text (str): The alternative text for the image.
    - path (str): The file path of the image.
    - link (str): The URL that the image should link to.

    Returns:
    - str: A string containing the Markdown-formatted code for the image with a link.
    """
    add_imge_code = f"[![{Alt_Text}]({path})]({link})"
    return add_imge_code

def readme_gen (name, save_path, Readme_top, readme_img_folder, config_dir, ):

    # var
    Full_readme_str =""
    Git_owner = read_config(config_dir, "readme", "github_user")
    repro_Git_owner = Git_owner
    discord_link = read_config(config_dir, "readme", "discord_link")
    discord_ID = read_config(config_dir, "readme", "discord_ID")
    Description = pyautogui.prompt(text='Description von der Repro', title='README.md' , default="Coming soon...")
    py_version = sys.version.split()[0]

    path_banner_img = copy_image(Readme_top, readme_img_folder)
    path_banner_img += os.path.sep + "Readme_top.png"
    readme_code = ""


    

    readme_code += add_image_to_markdown(f"github/{Git_owner}", f"https://raw.githubusercontent.com/{Git_owner}/{name}/main/README_img/Readme_top.png", f"https://github.com/{Git_owner}")+"\n"


    readme_code += f"\n# {name}\n\n"
    badge_line = ""

    Alt_text = f"downloads/total"
    path_img = f"https://img.shields.io/github/downloads/{Git_owner}/{name}/total"
    link_img = f"https://github.com/{Git_owner}/{name}/archive/refs/heads/main.zip"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/repo-size"
    path_img = f"https://img.shields.io/github/repo-size/{Git_owner}/{name}"
    link_img = f"https://github.com/{Git_owner}/{name}/archive/refs/heads/main.zip"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/license"
    path_img = f"https://img.shields.io/github/license/{Git_owner}/{name}"
    link_img = f"https://github.com/{Git_owner}/{name}/blob/main/LICENSE"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/last-commit" 
    path_img = f"https://img.shields.io/github/downloads/{Git_owner}/{name}/total"
    link_img = f"https://img.shields.io/github/issues/{Git_owner}/{name}?style=plastic"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/issues_open"
    path_img = f"https://img.shields.io/github/issues/{Git_owner}/{name}?style=plastic"
    link_img = f"https://img.shields.io/github/issues-raw/{Git_owner}/{name}"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"github/stars"
    path_img = f"https://img.shields.io/github/stars/{Git_owner}/{name}?style=social"
    link_img = f"https://github.com/{Git_owner}/{name}/stargazers"
    badge_line += add_image_to_markdown(Alt_text, path_img, link_img) + " "

    Alt_text = f"discord"
    path_img = f"{discord_link}"
    link_img = f"https://img.shields.io/discord/{discord_ID}"
    badge_line += add_image_to_markdown(Alt_text, link_img, path_img) + "\n"

    readme_code += badge_line +"\n"
    readme_code += Description +"\n"

    Table_of_Contents ="""## 📝 Table of Contents
+ [Demo / Working](#demo)
+ [Install](#usage)
+ [How it works](#Use)
+ [Lizenz](#Lizenz)"""

    readme_code += Table_of_Contents +"\n"

    rest_fill = f"""## 🎥 Demo / Working <a name = "demo"></a>
coming soon...

## 💻 Install <a name = "usage"></a>
```cmd
git clone https://github.com/{Git_owner}/{name}
pip install -r requirements.txt
```
## 💭 How it works <a name = "Use"></a>

start {name}.py directly from the folder or run in cmd:
```cmd
cd <local path of {name}>
python {name}.py
```

## 📚 Lizenz <a name = "Lizenz"></a>
MIT License

Copyright (c) 2023 {Git_owner}
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
    """
    readme_code += rest_fill +"\n"

    nice_end = """<p align="center">
<img src="https://raw.githubusercontent.com/NapoII/NapoII/233630a814f7979f575c7f764dbf1f4804b05332/Bottom.svg" alt="Github Stats" />
</p>
"""
    readme_code += nice_end
    Create_File("README.md", save_path, readme_code)
    return save_path