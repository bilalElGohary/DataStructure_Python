class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Runtime: O(n)
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.value))
            curr = curr.next
        return "[" + ", ".join(nodes) + "]"

    # Runtime: O(n)
    def __contains__(self, value):
        curr = self.head
        while curr:
            if curr.value == value: return True
            curr = curr.next
        return False

    # Runtime: O(1) (Optimized from O(n))
    def __len__(self):
        return self._size

    # Runtime: O(1)
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Runtime: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._size += 1

    # Runtime: O(n)
    def get_node(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    # Runtime: O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            curr = self.get_node(index)
            new_node = Node(value)
            new_node.previous = curr.previous
            new_node.next = curr
            curr.previous.next = new_node
            curr.previous = new_node
            self._size += 1

    # Runtime: O(n)
    def pop(self, index=None):
        if self._size == 0: raise IndexError("Pop from empty list")
        if index is None: index = self._size - 1
        
        target = self.get_node(index)
        if target.previous: target.previous.next = target.next
        else: self.head = target.next
            
        if target.next: target.next.previous = target.previous
        else: self.tail = target.previous
            
        self._size -= 1
        return target.value

    # Runtime: O(n)
    def delete(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                if curr.previous: curr.previous.next = curr.next
                else: self.head = curr.next
                
                if curr.next: curr.next.previous = curr.previous
                else: self.tail = curr.previous
                
                self._size -= 1
                return True
            curr = curr.next
        return False
