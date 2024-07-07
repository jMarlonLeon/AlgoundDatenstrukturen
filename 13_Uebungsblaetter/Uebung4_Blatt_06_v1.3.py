
class binärbaum:
    def __init__(self,wert):
        self.wert = wert
        self.links = None
        self.rechts = None

def abstand():
    print("\n \n \n")
    print("---------------------------------")
    print("\n \n \n")

# Illustration der Löschvorgänge 

# a. Zeichnen Sie den binären Suchbaum, der beim Einfügen der folgenden Schlüssel entsteht: 
# 23, 8, 25, 5, 20, 16, 12, 18, 14, 28, 26, 30, 36, 34, 38 (die Schlüssel werden in der gegebenen Reihenfolge eingefügt).

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

#       23
#     /    \
#    8      25
#   / \      \
#  5   20     28
#     /  \    / \
#    16  22  26  30
#   /  \          \
#  12  18          36
#    \            /  \
#    14          34  38


def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    print_tree(node.rechts, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.wert))

    print_tree(node.links, prefix + ("    " if is_left else "│   "), True)

print_tree(baum)


# b. Zeichnen Sie den Suchbaum, der nach dem Löschen des Knotens mit dem Schlüssel 25 entsteht.
abstand()

baum2 = binärbaum(23)
baum2.links = binärbaum(8)
baum2.links.links = binärbaum(5)
baum2.links.rechts = binärbaum(20)
baum2.links.rechts.links = binärbaum(16)
baum2.links.rechts.links.links = binärbaum(12)
baum2.links.rechts.links.links.rechts = binärbaum(14)
baum2.rechts = binärbaum(28)
baum2.rechts.links = binärbaum(26)
baum2.rechts.rechts = binärbaum(30)
baum2.rechts.rechts.links = binärbaum(36)
baum2.rechts.rechts.links.links = binärbaum(34)
baum2.rechts.rechts.links.rechts = binärbaum(38)

#       23
#     /    \
#    8      28
#   / \    /  \
#  5   20 26  30
#     /  \      \
#    16  22     36
#   /  \       /  \
#  12  18     34  38
#    \
#    14

print_tree(baum2)


# c. Zeichnen Sie den Suchbaum, der entsteht, wenn nun auch noch der Knoten mit dem Schlüssel 20 gelöscht wird.
abstand()

baum3 = binärbaum(23)
baum3.links = binärbaum(8)
baum3.links.links = binärbaum(5)
baum3.links.rechts = binärbaum(22)
baum3.links.rechts.links = binärbaum(16)
baum3.links.rechts.links.links = binärbaum(12)
baum3.links.rechts.links.links.rechts = binärbaum(14)
baum3.rechts = binärbaum(28)
baum3.rechts.links = binärbaum(26)
baum3.rechts.rechts = binärbaum(30)
baum3.rechts.rechts.links = binärbaum(36)
baum3.rechts.rechts.links.links = binärbaum(34)
baum3.rechts.rechts.links.rechts = binärbaum(38)

#       23
#     /    \
#    8      28
#   / \    /  \
#  5   22 26  30
#     /        \
#    16         36
#   /  \       /  \
#  12  18     34  38
#    \
#    14

print_tree(baum3)

# d. Zeichnen Sie den Suchbaum, der entsteht, wenn nun auch noch der Knoten mit dem Schlüssel 28 gelöscht wird.
abstand()

baum4 = binärbaum(23)
baum4.links = binärbaum(8)
baum4.links.links = binärbaum(5)
baum4.links.rechts = binärbaum(22)
baum4.links.rechts.links = binärbaum(16)
baum4.links.rechts.links.links = binärbaum(12)
baum4.links.rechts.links.links.rechts = binärbaum(14)
baum4.rechts = binärbaum(26)
baum4.rechts.links = binärbaum(30)
baum4.rechts.links.links = binärbaum(36)
baum4.rechts.links.links.links = binärbaum(34)
baum4.rechts.links.links.rechts = binärbaum(38)

#       23
#     /    \
#    8      26
#   / \       \
#  5   22      30
#     /         \
#    16          36
#   /  \        /  \
#  12  18      34  38
#    \
#    14

print_tree(baum4)

# e. Zeichnen Sie den Suchbaum, der entsteht, wenn nun auch noch der Knoten mit dem Schlüssel 8 gelöscht wird.
abstand()

baum5 = binärbaum(23)
baum5.links = binärbaum(12)
baum5.links.links = binärbaum(5)
baum5.links.links.links = binärbaum(14)
baum5.links.links.links.links = binärbaum(16)
baum5.links.links.links.links.links = binärbaum(22)
baum5.rechts = binärbaum(26)
baum5.rechts.links = binärbaum(30)
baum5.rechts.links.links = binärbaum(36)
baum5.rechts.links.links.links = binärbaum(34)
baum5.rechts.links.links.rechts = binärbaum(38)

#       23
#        \
#        12
#       /  \
#      5    14
#           /  \
#         16    22
#                \
#                26
#                 \
#                 30
#                 /  \
#                36  38
#                /
#               34

print_tree(baum5)
