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
#         50
#       /    \
#     25      75
#    /  \    /  \
#   12  37  62   87
#  / \    \    /
# 6  18   40  80

# Erzeuge Baum
baum = binary_tree(50)
baum.left = binary_tree(25)
baum.right = binary_tree(75)
baum.left.left = binary_tree(12)
baum.left.right = binary_tree(37)
baum.right.left = binary_tree(62)
baum.right.right = binary_tree(87)
baum.left.left.left = binary_tree(6)
baum.left.left.right = binary_tree(18)
baum.left.right.right = binary_tree(40)
baum.right.right.left = binary_tree(80)


print("Preorder Traversierung:", preorder_traversierung_als_array_ausgeben(baum))
print("Postorder Traversierung:", postorder_traversierung_als_array_ausgeben(baum))
print("Inorder Traversierung:", inorder_traversierung_als_array_ausgeben(baum))
