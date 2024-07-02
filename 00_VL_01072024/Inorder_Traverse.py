
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Was ist diese Klasse ? : Diese Klasse ist ein Knoten in einem binären Baum

def meinefunktion(node):
    if node:
        meinefunktion(node.left)
        print(node.data, end=" ")
        meinefunktion(node.right)

# Was macht meinefunktion() ?
# meinefunktion = Inorder Traversal


# Was ist das ? : Ein gerichteter, binärer Suchbaum
root = Node(1)
root.left = Node(2)
root.right = Node(3)
