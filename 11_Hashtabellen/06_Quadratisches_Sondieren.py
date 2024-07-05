
# Hashtabelle mit offener Adressierung und quadratischer Sondierung im Kollisionsfall
# Quadratische Sondierung: h(k, i) = (h'(k) + i^2) mod m
# Der Index wird um i^2 erhöht, bis ein freier Platz gefunden wird

# -----------------------------------------------------------------------------------

# Größe der Hashtabelle
GROESSE = 10

# Initialisierung der Hashtabelle
hashtabelle = [None] * GROESSE

# Hash-Funktion
def hash_funktion(schluessel):
    # alternativ zur hash() für ganzen string geht auch ord() für den ersten Buchstaben
    return hash(schluessel) % GROESSE

# Quadratische Sondierung
def quadratische_sondierung(index, i):
    return (index + i * i) % GROESSE

# Einfügen eines Schlüssel-Wert-Paares
def einfuegen(schluessel, wert):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = quadratische_sondierung(index, i)
        if hashtabelle[probe_index] is None or hashtabelle[probe_index][0] == schluessel:
            hashtabelle[probe_index] = (schluessel, wert)
            return True
        i += 1
    return False  # Hashtabelle ist voll

# Suchen eines Schlüssels
def suchen(schluessel):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = quadratische_sondierung(index, i)
        if hashtabelle[probe_index] is None:
            return None
        if hashtabelle[probe_index][0] == schluessel:
            return hashtabelle[probe_index][1]
        i += 1
    return None  # Schlüssel nicht gefunden

# Löschen eines Schlüssel-Wert-Paares
def loeschen(schluessel):
    index = hash_funktion(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = quadratische_sondierung(index, i)
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
