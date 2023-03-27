import shutil

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



A = "E:\Pr0grame\My_ Pyhton\work_in_progress\[New-Template_PY]\Work_Folder\Readme_top.png"
B = "E:\Pr0grame\My_ Pyhton\work_in_progress\[New-Template_PY]\ss"

copy_image(A,B)