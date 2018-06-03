# Class used to make the tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def isBST(root, min, max):
    if root == None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)


def check_BST(root):
    return isBST(root, float('-inf'), float('inf'))

root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)

print("BST?"),
print(bool(check_BST(root)))
