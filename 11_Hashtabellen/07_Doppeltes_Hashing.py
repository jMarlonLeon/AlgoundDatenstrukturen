
# Hastabelle mit offener Adressierung und doppeltem Hashing im Kollisionsfall
# Doppeltes Hashing: h(k, i) = (h1(k) + i * h2(k)) mod m
# h1(k) = k mod m
# h2(k) = 1 + (k mod (m - 1))
# Der Index (hash1) wird um i * hash2 erhöht, bis ein freier Platz gefunden wird

# ---------------------------------------------------------------------------------

# Größe der Hashtabelle
GROESSE = 10

# Initialisierung der Hashtabelle
hashtabelle = [None] * GROESSE

# Primäre Hash-Funktion
def hash_funktion1(schluessel):
    return ord(schluessel[0]) % GROESSE

# Sekundäre Hash-Funktion
def hash_funktion2(schluessel):
    return 1 + (ord(schluessel[0]) % (GROESSE - 1))

def einfuegen(schluessel, wert):
    index1 = hash_funktion1(schluessel)
    index2 = hash_funktion2(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = (index1 + i * index2) % GROESSE
        if hashtabelle[probe_index] is None or hashtabelle[probe_index][0] == schluessel:
            hashtabelle[probe_index] = (schluessel, wert)
            return True
        i += 1
    return False  # Hashtabelle ist voll

def suchen(schluessel):
    index1 = hash_funktion1(schluessel)
    index2 = hash_funktion2(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = (index1 + i * index2) % GROESSE
        if hashtabelle[probe_index] is None:
            return None
        if hashtabelle[probe_index][0] == schluessel:
            return hashtabelle[probe_index][1]
        i += 1
    return None  # Schlüssel nicht gefunden

def loeschen(schluessel):
    index1 = hash_funktion1(schluessel)
    index2 = hash_funktion2(schluessel)
    i = 0
    while i < GROESSE:
        probe_index = (index1 + i * index2) % GROESSE
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