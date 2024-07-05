
# Hasfunktion mit Offener Adressierung und linearer Sondierung im Kollisionsfall
# Lineare Sondierung: h(k, i) = (h'(k) + i) mod m
# Der Index wird um i erhöht, bis ein freier Platz gefunden wird

# ---------------------------------------------------------------------------------

# Größe der Hashtabelle
GROESSE = 10

hashtabelle = [None] * GROESSE

# Hash-Funktion
def hash_funktion(schluessel):
    # alternativ zur hash() für ganzen string geht auch ord() für den ersten Buchstaben
    return hash(schluessel) % GROESSE

def lineare_sondierung(index, i):
    return (index + i) % GROESSE

def einfuegen(schluessel, wert):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = lineare_sondierung(index, i)
        if hashtabelle[probe_index] is None or hashtabelle[probe_index][0] == schluessel:
            hashtabelle[probe_index] = (schluessel, wert)
            return True
        i += 1
    return False  # Hashtabelle ist voll

def suchen(schluessel):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = lineare_sondierung(index, i)
        if hashtabelle[probe_index] is None:
            return None
        if hashtabelle[probe_index][0] == schluessel:
            return hashtabelle[probe_index][1]
        i += 1
    return None  # Schlüssel nicht gefunden

def loeschen(schluessel):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = lineare_sondierung(index, i)
        if hashtabelle[probe_index] is None:
            return False
        if hashtabelle[probe_index][0] == schluessel:
            hashtabelle[probe_index] = None
            return True
        i += 1
    return False  # Schlüssel nicht gefunden


# ---------------------------------------------------------------------------------

einfuegen("Apfel", 1)
einfuegen("Banane", 2)
einfuegen("Citrone", 3)

print("Suche 'Banane':", suchen("Banane"))
print("Suche 'Orange':", suchen("Orange"))

loeschen("Banane")