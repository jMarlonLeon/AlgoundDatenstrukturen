
# Breitensuche (BFS) in einem Binärbaum
# Breitensuche funktioniert wie folgt:
# 1. Starte bei der Wurzel
# 2. Besuche alle Kinder der Wurzel
# 3. Besuche alle Kinder der Kinder der Wurzel
# 4. usw.

class binärbaum:
    def __init__(self, schlüssel):
        self.schlüssel = schlüssel
        self.links = None
        self.rechts = None

def bfs(root, schlüssel):
    # Erstelle eine Liste, die die Knoten enthält, die noch besucht werden müssen
    queue = [root]
    # Solange die Liste nicht leer ist
    while queue:
        # Entferne den ersten Knoten aus der Liste
        knoten = queue.pop(0)
        # Wenn der Schlüssel des Knotens dem gesuchten Schlüssel entspricht, gib den Knoten zurück
        if knoten.schlüssel == schlüssel:
            return knoten
        # Füge die Kinder des Knotens zur Liste hinzu
        if knoten.links:
            queue.append(knoten.links)
        if knoten.rechts:
            queue.append(knoten.rechts)
    # Wenn der Schlüssel nicht gefunden wurde, gib None zurück
    return None

# Erstellen des Baumes
baum = binärbaum(23)
baum.links = binärbaum(8)
baum.rechts = binärbaum(25)
baum.links.links = binärbaum(5)
baum.links.rechts = binärbaum(20)
baum.links.rechts.links = binärbaum(16)
baum.links.rechts.links.links = binärbaum(12)
baum.links.rechts.links.links.rechts = binärbaum(14)
baum.rechts.rechts = binärbaum(28)
baum.rechts.rechts.links = binärbaum(26)
baum.rechts.rechts.rechts = binärbaum(30)
baum.rechts.rechts.rechts.links = binärbaum(36)
baum.rechts.rechts.rechts.links.links = binärbaum(34)
baum.rechts.rechts.rechts.links.rechts = binärbaum(38)


# Breitensuche im Baum
print(bfs(baum, 25).schlüssel) # Ausgabe: 25
