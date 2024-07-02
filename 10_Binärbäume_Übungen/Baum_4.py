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
#           45
#         /    \
#       30      60
#      /  \    /  \
#    15   35  55   75
#   /  \    \     /  \
#  8   20   40   70   80
# /   /             \
# 3  18             78

# Erzeuge Baum
baum = binary_tree(45)
baum.left = binary_tree(30)
baum.right = binary_tree(60)
baum.left.left = binary_tree(15)
baum.left.right = binary_tree(35)
baum.right.left = binary_tree(55)
baum.right.right = binary_tree(75)
baum.left.left.left = binary_tree(8)
baum.left.left.left.left = binary_tree(3)
baum.left.left.right = binary_tree(20)
baum.left.left.right.left = binary_tree(18)
baum.left.right.right = binary_tree(40)
baum.right.right.left = binary_tree(70)
baum.right.right.left.right = binary_tree(78)
baum.right.right.right = binary_tree(80)



print("Preorder Traversierung:", preorder_traversierung_als_array_ausgeben(baum))
print("Postorder Traversierung:", postorder_traversierung_als_array_ausgeben(baum))
print("Inorder Traversierung:", inorder_traversierung_als_array_ausgeben(baum))
