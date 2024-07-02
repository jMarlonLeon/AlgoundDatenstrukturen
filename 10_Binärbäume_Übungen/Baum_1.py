class binary_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversierung_als_array_ausgeben(tree):
    if tree is None:
        return []
    return [tree.value] + preorder_traversierung_als_array_ausgeben(tree.left) + preorder_traversierung_als_array_ausgeben(tree.right)

def postorder_traversierung_als_array_ausgeben(tree):
    if tree is None:
        return []
    return postorder_traversierung_als_array_ausgeben(tree.left) + postorder_traversierung_als_array_ausgeben(tree.right) + [tree.value]

def inorder_traversierung_als_array_ausgeben(tree):
    if tree is None:
        return []
    return inorder_traversierung_als_array_ausgeben(tree.left) + [tree.value] + inorder_traversierung_als_array_ausgeben(tree.right)

# Erzeuge Baum
#          20
#        /    \
#      10      30
#     /  \    /  \
#    5   15  25   35
#   / \    \
#   2  7   17

# Erzeuge Baum
baum = binary_tree(20)
baum.left = binary_tree(10)
baum.right = binary_tree(30)
baum.left.left = binary_tree(5)
baum.left.right = binary_tree(15)
baum.right.left = binary_tree(25)
baum.right.right = binary_tree(35)
baum.left.left.left = binary_tree(2)
baum.left.left.right = binary_tree(7)
baum.left.right.right = binary_tree(17)

print("Preorder Traversierung:", preorder_traversierung_als_array_ausgeben(baum))
print("Postorder Traversierung:", postorder_traversierung_als_array_ausgeben(baum))
print("Inorder Traversierung:", inorder_traversierung_als_array_ausgeben(baum))
