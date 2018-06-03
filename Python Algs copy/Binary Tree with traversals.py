class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data),
       inOrder(root.right)

def preOrder(root):
   if root:
       print (root.data),
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print (root.data),



#making the tree
# root = Node(14)
#
# root.left = Node(12)
# root.left.left = Node(9)
# root.left.right = Node(13)
# root.left.left.left = Node(7)
# root.left.left.right = Node(10)
# root.left.left.right.left = Node(8)
# root.left.left.right.right = Node(11)
#
# root.right = Node(19)
# root.right.left = Node(16)
# root.right.right = Node(21)
#
# root.right.left.left = Node(15)
# root.right.left.right = Node(17)
#
# root.right.right.left = Node(20)
# root.right.right.right = Node(24)

def print_bst(tree):
    current_level = [tree]
    while current_level:
        next_level = []
        for node in current_level:
            print(node.data),
            # Logic to start building the next level
            ##Added
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
                    ####

        print() # Print a newline between levels
        current_level = next_level

root = Node(6)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)

root.right.right = Node(10)
root.right.right.left = Node(9)
root.right.right.right = Node(11)

#print_bst(root)


#print "In:", inOrder(root)
# print "Pre:", preOrder(root)
# print "Post:", postOrder(root)