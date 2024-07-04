
# Laufzeit: längere Laufzeit als Divisionsmethode (mod)
# Vorteil: Wert von m spielt keine kritische Rolle (oft wird m als potenz von 2 gewählt)

# Multiplikationsmethode: h(k) = floor(m * (k * A mod 1))
def hash_function(name, m):
    first_letter = ord(name[0])
    A = (5 ** 0.5 - 1) / 2                      # Muss im Bereich von 0 und 1 liegen
    hashwert = ((first_letter * A) % 1 ) * m    # Modulo 1 ergibt den Nachkommawert, der dann mit m multipliziert wird
                                                # hashwert = h( 𝑘 )= ⌊ 𝑚( 𝑘𝐴mod 1) ⌋
    return  int(hashwert)                       # Der Wert wird auf den nächsten ganzzahligen Wert abgerundet

def insert(name, number):
    index = hash_function(name, len(hashtable))
    hashtable[index].append((name, number))

def find(name):
    index = hash_function(name, len(hashtable))
    for entry in hashtable[index]:
        if entry[0] == name:
            return entry[1]
    return "Nicht gefunden"

hashtable = [[] for _ in range(10)]

# ------------------------------------------

insert("Alice", "123-456-7890")
insert("Bob", "234-567-8901")
insert("Charlie", "345-678-9012")
insert("David", "456-789-0123")

print(find("Alice"))  # Ausgabe: 123-456-7890
print(find("Bob"))    # Ausgabe: 234-567-8901
