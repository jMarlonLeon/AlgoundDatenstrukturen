
GROESSE = 11

hashtabelle = [None] * GROESSE

def hilfshashfunktion(schluessel):
    hashwert = schluessel % GROESSE
    return hashwert

def hash_lineares_sondieren(schluessel, i):
    return (hilfshashfunktion(schluessel) + i) % GROESSE

def einfuegen(schluessel):
    index = hilfshashfunktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = hash_lineares_sondieren(index, i)
        if hashtabelle[probe_index] is None or hashtabelle[probe_index] == schluessel:
            hashtabelle[probe_index] = schluessel
            return True
        i += 1
    return False  # Hashtabelle ist voll

def loeschen(schluessel):
    index = hilfshashfunktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = hash_lineares_sondieren(index, i)
        if hashtabelle[probe_index] is None:
            return False
        
        if hashtabelle[probe_index] == schluessel:
            hashtabelle[probe_index] = None
            return True
        i += 1
    return False  # Schlüssel nicht gefunden

def anzeigen():
    for Slot, wert in enumerate(hashtabelle):
        if wert is not None:
            print(f"Slot {Slot}: {wert}")

einfuegewerte = [10,22,31,4,15,28,17,88,59]

for wert in einfuegewerte:
    einfuegen(wert)

print("Hashtabelle nach dem Einfügen der Werte:")
anzeigen()