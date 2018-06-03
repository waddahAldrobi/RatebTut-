# tree.py
""" Binary Search Tree implementation. """


class BinarySearchTree(object):
    """ Store values within a binary tree structure for later lookup. """
    def __init__(self):
        self.root = None
        self._size = 0  # Do not want to directly modify this

    @property
    def length(self):
        return self._size

    def __contains__(self, key):
        return self._get(key, self.root) is not None

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        return self.root.__iter__()

    def __len__(self):
        return self._size

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __str__(self):
        if self.root:
            return self.root.__str__()
        else:
            return 'Empty Tree.'

    def delete(self, key):
        if self._size > 1:
            to_remove = self._get(key, self.root)

            if to_remove:
                self.remove(to_remove)
                self._size -= 1
            else:
                raise KeyError(f'Error, {key} is not in the tree.')
        elif self._size == 1 and self.root.key == key:
            self.root = None
            self._size = 0
        else:
            raise KeyError(f'Error, {key} is not in the tree.')

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
            else:
                return None
        return None

    def insert(self, key, value):
        if self.root:
            # Call a recursive insert
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value)
        self._size += 1

    def remove(self, node):
        if node.is_leaf():
            # Simple, this node has no children
            if node.is_left_child():
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        else:
            # Node only has one child
            if node.has_left_child():
                if node.is_left_child():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:
                    # Current node has no parent, it's the root
                    node.replace_data(
                        node.left_child.key,
                        node.left_child.value,
                        left=node.left_child.left,
                        right=node.left_child.right
                    )
            elif node.has_both_children():
                # Interior
                succ = node.find_successor()
                succ.splice_out()
                node.key = succ.key
                node.value = succ.value
            else:
                if node.is_left_child():
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:
                    # Current node has no parent, it's the root
                    node.replace_data(
                        node.right_child.key,
                        node.right_child.value,
                        left=node.right_child.left,
                        right=node.right_child.right
                    )

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def _insert(self, key, value, current_node):
        """ Recursively search for a place to insert the key value pair """
        if key < current_node.key:
            if current_node.has_left_child():
                self._insert(key, value, current_node.left_child)
            else:
                current_node.left_child = Node(
                    key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._insert(key, value, current_node.right_child)
            else:
                current_node.right_child = Node(
                    key, value, parent=current_node)


class Node(object):
    """ A node within a binary tree. """
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem

        yield self.key

        if self.has_right_child():
            for elem in self.right_child:
                yield elem

    def __repr__(self):
        return f'<Node: [{self.key}: {self.value}]>'

    def __str__(self, depth=0):
        ret = ''

        # Print the right branch
        if self.right_child is not None:
            ret += self.right_child.__str__(depth + 1)

        # Print own value
        ret += '\n' + ("\t" * depth) + f'{self.value}'

        # Print left branch
        if self.left_child is not None:
            ret += self.left_child.__str__(depth + 1)

        return ret

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def has_both_children(self):
        return self.left_child is not None and self.right_child is not None

    def has_children(self):
        return not self.is_leaf

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def replace_data(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right

        if self.has_left_child():
            self.left_child.parent = self

        if self.has_right_child():
            self.right_child.parent = self

        return self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None

        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
