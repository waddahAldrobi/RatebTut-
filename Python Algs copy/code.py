# Cell #1 Node

def is_root(self):
    return self.parent is None
    
def is_leaf(self):
    return self.left_child is None and self.right_child is None































# Cell #2 BST _insert()
def _insert(self, key, value, current_node):
    if key < current_node.key:
        # Key is less than the current nodes key, it should go left
        if not current_node.has_left_child():
            current_node.left_child = Node(key, value, parent=current_node)
        else:
            self._insert(key, value, current_node=current_node.left_child)
    else:
        # Key is greater than the current_nodes key
        if not current_node.has_right_child():
            current_node.right_child = Node(key, value, parent=current_node)
        else:
            self._insert(key, value, current_node=current_node.right_child)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
# Cell #3 BST _get()
def _get(self, key, current_node):
    # What do we do if current node is None? What does that mean?
    if current_node is None:
        return None
            
    elif current_node.key == key:
        # We found it!
        return current_node

    # How do we traverse the tree?
    elif key < current_node.key:
        return self._get(key, current_node=current_node.left_child)
    else:
        return self._get(key, current_node=current_node.right_child)            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Cell #4 get and set methods
def __getitem__(self, key):        
    return self.get(key)
    
def __setitem__(self, key, value):
    return self.insert(key, value)











































# Cell #5 Deleting nodes
def delete(self, key):
    if self.length > 1:
        to_remove = self._get(key, self.root)  # First find the node we want to remove
        if to_remove is None:
            raise KeyError(f'Key {key} is not in the tree.')
        else:
            self.remove(to_remove)
            self._size -= 1
    else:
        if self.root is not None:
            self.root = None
            self._size = 0
        else:
            raise KeyError(f'Key {key} is not in the tree.')
            
def remove(self, node):
    # Handle our three cases
    if to_remove.is_leaf():
        # No children! What do we do?
        if node.is_left_child():
            node.parent.left_child = None
        else:
            node.parent.right_child = None
            
    elif to_remove.has_both_children():
        # This node has two children
        succ = node.find_successor()
        succ.splice_out()
        node.key = succ.key
        node.value = succ.value
    else:
        # First check if we're the root
        if node.parent is None:
            # Current node has no parent, it's the root
            # Replace is with the right child, but why?
            node.replace_data(
                node.right_child.key,
                node.right_child.value,
                left=node.right_child.left,
                right=node.right_child.right
            )
        elif node.is_left_child():
            node.right_child.parent = node.parent
            node.parent.left_child = node.right_child
        elif node.is_right_child():
            node.right_child.parent = node.parent
            node.parent.right_child = node.right_child