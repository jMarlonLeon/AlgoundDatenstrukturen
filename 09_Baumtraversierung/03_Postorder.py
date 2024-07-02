
class binary_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversierung(tree):
    if tree is None:
        return
    postorder_traversierung(tree.left)
    postorder_traversierung(tree.right)
    print(tree.value)

# Erzeuge Baum
baum = binary_tree(1)
baum.left = binary_tree(2)
baum.right = binary_tree(3)
baum.left.left = binary_tree(4)
baum.left.right = binary_tree(5)
baum.right.left = binary_tree(6)
baum.right.right = binary_tree(7)

# baum grafisch ausgeben
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

print("Postorder Traversierung:")
postorder_traversierung(baum)
