
# Laufzeit: kürzere Laufzeit als Multiplikationsmethode
# Es müssen einige Werte für m vermieden werden: m sollte nicht eine Potenz von 2 sein,
# da sonst nur die unteren Bits der Hashfunktion verwendet werden.
# wenn m eine Primzahl ist, sollte A nicht ein Vielfaches von m sein.
# wenn k eine zeichenkette ist, sollte m=2^p-1 vermieden werden, da permutationen die gleichen Hashwerte ergeben.

# Empfohlen wird m als Primzahl zu wählen, die nicht zu nahe an einer Potenz von 2 liegt.


# Hashfunktion: Erster Buchstabe des Namens (Grossbuchstabe) (ASCII-Wert), Modulo m (anzahl der Slots)
def hash_function(name, m):
    first_letter = ord(name[0])
    return first_letter % m

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
