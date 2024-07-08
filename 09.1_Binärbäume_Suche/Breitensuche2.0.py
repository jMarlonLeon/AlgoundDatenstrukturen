
class binärbaum:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    
def breitensuche(wurzel, key):
    warteschlange = [wurzel]
    print("Wurzel:",warteschlange[0].key)
    
    while len(warteschlange) != 0:
        
        knoten = warteschlange.pop(0)
        print("Knoten pop:",knoten.key)
        if knoten.key == key:
            return knoten
        if knoten.left:
            warteschlange.append(knoten.left)
        if knoten.right:
            warteschlange.append(knoten.right)
        
        for node in warteschlange:
            print(node.key)
        print("-----")

    return None

# Baum als Graphik
#          23
#        /    \
#       8      25
#      / \       \
#     5  20       28
#        /         / \
#       16        26 30
#      / \            /
#     12  20         36
#        / \        / \
#       14  16     34 38


# Erstellen des Baumes
baum = binärbaum(23)
baum.left = binärbaum(8)
baum.right = binärbaum(25)
baum.left.left = binärbaum(5)
baum.left.right = binärbaum(20)
baum.left.right.left = binärbaum(16)
baum.left.right.left.left = binärbaum(12)
baum.left.right.left.left.right = binärbaum(14)
baum.right.right = binärbaum(28)
baum.right.right.left = binärbaum(26)
baum.right.right.right = binärbaum(30)
baum.right.right.right.left = binärbaum(36)
baum.right.right.right.left.left = binärbaum(34)
baum.right.right.right.left.right = binärbaum(38)

# Breitensuche im Baum
print(breitensuche(baum, 38).key) # Ausgabe: 25


