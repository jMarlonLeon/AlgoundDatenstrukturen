# Größe der Hashtabelle
GROESSE = 9

# Initialisierung der Hashtabelle
hashtabelle = [[] for _ in range(GROESSE)]

# Hash-Funktion
def hash_funktion(k):
    return k % GROESSE

# Einfügen eines Wertes
def einfuegen(wert):
    index = hash_funktion(wert)
    hashtabelle[index].append(wert)

# Anzeigen der Hashtabelle
def anzeigen():
    for i, slot in enumerate(hashtabelle):
        print(f"Slot {i}: {slot}")

# Werte sind sowohl schlüssel als auch wert, daher kein Schlüssel-Wert-Paar
werte = [5, 28, 19, 15, 20, 33, 12, 17, 10]
for wert in werte:
    einfuegen(wert)

print("Hashtabelle nach dem Einfügen der Werte:")
anzeigen()
