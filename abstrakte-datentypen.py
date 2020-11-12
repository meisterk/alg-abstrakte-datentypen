# Sequenz, Array, List
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
stapel = []
stapel.append('Anna')
stapel.append('Berta')
stapel.append('Carla')

print(stapel.pop())
print(stapel)

## Anwendung für Stapel: Undo-Funktion

