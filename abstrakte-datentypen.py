# Sequenz, Array, List
print("#### Sequenz ####")
liste = ["Anna", "Berta", "Carla", "Dieter"]

## Lesezugriff über Index
print(liste[0]) # "Anna"

## Schreibzugriff über Index
liste[1] = "Bertram"
print(liste)

## Löschen des Elements mit Index 1
neue_liste = []
for i in range(0,len(liste)):
    if i != 1:
        neue_liste.append(liste[i])
print(neue_liste)

## Einfügen eines Elements am Index 1
neue_liste2 = []
for i in range(0,len(neue_liste)):
    if i == 1:
        neue_liste2.append("Berta")                
    neue_liste2.append(neue_liste[i])
print(neue_liste2)


# Stack, Stapel, LIFO (Last In First Out)
print("#### Stapel ####")
stapel = []

## Drauflegen (push)
stapel.append('Anna')
stapel.append('Berta')
stapel.append('Carla')

## oberstes Element entfernen
print(stapel.pop())
print(stapel)

## Anwendung für Stapel: Undo-Funktion


# Queue, Warteschlange, FIFO (First In First Out)
print("#### Schlange ####")
schlange = []

## Element an Schlange dranhängen
schlange.append('Anna')
schlange.append('Berta')
schlange.append('Carla')
print(schlange)

## Erstes Element der Schlange entfernen
print(schlange.pop(0))
print(schlange)

# Dictionary, Key-Value-Store
print("#### Dictionary ####")
woerterbuch = { "Hallo":"hello", "Katze":"cat", "Hund":"dog", "Maus":"mouse" }

## Lesezugriff
print(woerterbuch["Katze"])
print(woerterbuch["Maus"])

## Neues Paar hinzufügen
woerterbuch["Haus"] = "house"

## Vorhandenes Paar löschen
woerterbuch.pop('Haus', None)

if "Haus" in woerterbuch:
    print(woerterbuch["Haus"])
else:
    print("Keine Ahnung!")

# Set, Menge
print("#### Set, Menge ####")
menge = {"Anna", "Berta", "Carla"}

# Element hinzufügen
menge.add("Alf")
menge.add("Anna") # Wird nicht nochmal hinzugefügt, weil es schon drin ist
menge.add("anna") # Wird hinzugefügt, weil es noch nicht drin ist
print(menge)

# Element entfernen
menge.remove("Berta")
print(menge)

# Ist Element in Menge
if "Berta" in menge:
    print("Ist drin")
else:
    print("Ist nicht drin")