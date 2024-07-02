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
#          40
#        /    \
#      20      60
#     /  \    /  \
#    10  30  50   70
#   /      \       \
#  5       35       80
# / \              /
# 2   7           75

# Erzeuge Baum
baum = binary_tree(40)
baum.left = binary_tree(20)
baum.right = binary_tree(60)
baum.left.left = binary_tree(10)
baum.left.right = binary_tree(30)
baum.right.left = binary_tree(50)
baum.right.right = binary_tree(70)
baum.left.left.left = binary_tree(5)
baum.left.right.right = binary_tree(35)
baum.right.right.right = binary_tree(80)
baum.left.left.left.left = binary_tree(2)
baum.left.left.left.right = binary_tree(7)
baum.right.right.right.left = binary_tree(75)



print("Preorder Traversierung:", preorder_traversierung_als_array_ausgeben(baum))
print("Postorder Traversierung:", postorder_traversierung_als_array_ausgeben(baum))
print("Inorder Traversierung:", inorder_traversierung_als_array_ausgeben(baum))
