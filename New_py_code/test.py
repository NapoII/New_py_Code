from datetime import datetime

# Aktuelles Datum und Uhrzeit abrufen
aktuelles_datum = datetime.now()

# Monat ausgeschrieben abrufen
monat_ausgeschrieben = aktuelles_datum.strftime("%d.%B.%Y")

# Ausgabe des ausgeschriebenen Monats
print("Aktueller Monat ausgeschrieben:", monat_ausgeschrieben)
