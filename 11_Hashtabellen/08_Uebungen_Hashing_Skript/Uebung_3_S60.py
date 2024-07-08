from math import sqrt, floor

GROESSE = 1000

hashtabelle = [None] * GROESSE

def hashfunktion(schluessel):
    A = (sqrt(5) -1) /2
    # alternative zu floor geht auch int() oder // 1
    hashwert = (GROESSE * (schluessel * A % 1))
    return hashwert

def einfuegen(schluessel):
    index = hashfunktion(schluessel)
    hashtabelle[index] = schluessel

def suchen(schluessel):
    index = hashfunktion(schluessel)
    return hashtabelle[index]

def ausgeben():
    for Slot, wert in enumerate(hashtabelle):
        if wert is not None:
            print(f"Slot {Slot}: {wert}")

einfuegewerte = [61,62,63,64,65]

for wert in einfuegewerte:
    einfuegen(wert)

ausgeben()

        
