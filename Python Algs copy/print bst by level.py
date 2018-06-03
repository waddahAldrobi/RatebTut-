def print_bst(tree):
    current_level = [tree.root]
    while current_level:
        next_level = []
        for node in current_level:
            print(node.value,end='')
            # Logic to start building the next level
            ##Added
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
                    ####

        print() # Print a newline between levels
        current_level = next_level



