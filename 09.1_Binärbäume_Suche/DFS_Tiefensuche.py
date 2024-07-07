
# Tiefensuche (DFS) in einem Binärbaum
# Tiefensuche funktioniert wie folgt:
# 1. Starte bei der Wurzel
# 2. Besuche den linken Teilbaum
# 3. Besuche den rechten Teilbaum
# 4. usw.

class binärbaum:
    def __init__(self, schlüssel):
        self.schlüssel = schlüssel
        self.links = None
        self.rechts = None

def dfs(knoten, schlüssel):
    # Wenn der Knoten None ist, gib None zurück
    if knoten is None:
        return None
    # Wenn der Schlüssel des Knotens dem gesuchten Schlüssel entspricht, gib den Knoten zurück
    if knoten.schlüssel == schlüssel:
        return knoten
    # Führe die Tiefensuche rekursiv für den linken Teilbaum durch
    links = dfs(knoten.links, schlüssel)
    # Führe die Tiefensuche rekursiv für den rechten Teilbaum durch
    rechts = dfs(knoten.rechts, schlüssel)
    # Wenn der Schlüssel im linken Teilbaum gefunden wurde, gib den Knoten zurück
    if links:
        return links
    # Wenn der Schlüssel im rechten Teilbaum gefunden wurde, gib den Knoten zurück
    if rechts:
        return rechts
    # Wenn der Schlüssel weder im linken noch im rechten Teilbaum gefunden wurde, gib None zurück
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

# Tiefensuche im Baum
print(dfs(baum, 25).schlüssel) # Ausgabe: 25