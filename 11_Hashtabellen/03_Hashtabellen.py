
# Hashfunktion: Erste Buchstabe des Namens, Position im Alphabet, Modulo 10
def hash_function(name):
    first_letter = name[0].upper()
    letter_position = ord(first_letter) - ord('A') + 1
    return letter_position % 10

def insert(name, number):
    index = hash_function(name)
    hashtable[index].append((name, number))

def find(name):
    index = hash_function(name)
    for entry in hashtable[index]:
        if entry[0] == name:
            return entry[1]
    return "Nicht gefunden"

hashtable = [[] for _ in range(10)]

insert("Alice", "123-456-7890")
insert("Bob", "234-567-8901")
insert("Charlie", "345-678-9012")
insert("David", "456-789-0123")

print(find("Alice"))  # Ausgabe: 123-456-7890
print(find("Bob"))    # Ausgabe: 234-567-8901

