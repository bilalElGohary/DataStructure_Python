class Node:
    def __init__(self, key):
        self.key = key
        self.value = None
        self.right = None
        self.left = None
        self.parent = None
        
    def __repr__(self):
        return f"({self.key}, {self.value})"

class BST:
    def __init__(self):
        self.root = None
    
    # runtime:
    def __contains__(self, key):
        current = self.root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False
            
    # runtime:
    def __iter__(self):
        pass
    
    # runtime:
    def __repr__(self):
        pass
    
    # runtime:
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = Node(key)
                        current.left.value = value
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                        
                elif key > current.key:
                    if current.right is None:
                        current.right = Node(key)
                        current.right.value = value
                        current.right.parent = current
                        break
                    else:
                        current = current.right
                
                else:
                    current.value = value
                    break

                
    # runtime:
    def search(self, key):
        current = self.root
        while True:
            if current is None or current.key == key:
                return current
            elif key < current.key:
                if current.left is None:
                    return None
                else:
                    current = current.left
            else:
                if current.right is None:
                    return None
                else:
                    current = current.right
    
    # runtime:
    def delete(self, key):
        node = self.search(key)
        if node is None:
            raise KeyError("Theres no node with this key.")
        self._delete(node)
    
    # runtime:
    def traverse(self, order):
        pass
    
    # runtime:
    def isEmpty(self):
        pass
    
    # helper methods
    def _delete(self, node):
        # On leaf nodes
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None
                
        # On one child node
        elif node.left is None or node.right is None:
            child = node.left if node.left is not None else node.right
            if node.parent is None:
                child.parent = None
                self.root = child
            else:
                if node.parent.right == node:
                    node.parent.right = child
                else:
                    node.parent.left = child
                child.parent = node.parent
            node.parent = node.left = node.right = None

        # On two child node
        else:
            successor = self._successor(node)
            node.key = successor.key
            node.value = successor.value
            self.delete(successor)
            
    def _successor(self, node):
        if node is None:
            raise ValueError("Can not find successor of None")
        if node.right is None:
            return None
        else:
            current = node.right
            while current.left is not None:
                current = current.left
            return current
    
    def _predecessor(self, node):
        if node is None:
            raise ValueError("Can not find predecessor of None")
        if node.left is None:
            return None
        else:
            current = node.left 
            while current.right is not None:
                current = current.right
            return current

    
    def _inOrderTraverser(self):
        pass
    
    def _preOrderTraverser(self):
        pass
    
    def _postOrderTraverser(self):
        pass

    
if __name__ == "__main__":
    pass