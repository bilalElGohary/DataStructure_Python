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
        pass
    
    # runtime:
    def __iter__(self):
        pass
    
    # runtime:
    def __repr__(self):
        pass
    
    # runtime:
    def insert(self, key, value):
        pass
    
    # runtime:
    def search(self, key):
        pass
    
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