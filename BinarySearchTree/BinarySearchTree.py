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
        pass
    
    # runtime:
    def traverse(self, order):
        pass
    
    # runtime:
    def isEmpty(self):
        pass
    
    # helper methods
    def _delete(self, key):
        pass
    
    def _successor(self, node):
        pass
    
    def _predecessor(self, node):
        pass
    
    def _inOrderTraverser(self):
        pass
    
    def _preOrderTraverser(self):
        pass
    
    def _postOrderTraverser(self):
        pass

    
if __name__ == "__main__":
    pass