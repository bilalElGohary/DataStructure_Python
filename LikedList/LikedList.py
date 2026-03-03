class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # runtime: O(n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            returnString = f"[{last.value}"
            while last.next is not None:
                last = last.next
                returnString += f", {last.value}"
        returnString += "]"
        return returnString

    # runtime: O(n)
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # runtime: O(n)
    def __len__(self):
        count = 0
        last = self.head
        while last.next is not None:
            count += 1
            last = last.next
        return count

    # runtime: O(n)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # runtime: O(n)
    def pop(self, index):
        last = self.head
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
        if last.next is None:
            raise ValueError("Index out of bounds")
        else:
            last.next = last.next.next

    # runtime: O(1)
    def perpend(self, value):
        firstNode = Node(value)
        firstNode.next = self.head
        self.head = firstNode

    # runtime: O(n)
    def insert(self, value, index):
        last = self.head
        if index == 0:
            self.perpend(value)
        else:
            if last is None:
                raise ValueError("Index out of bounds")
            else:
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                node = Node(value)
                node.next = last.next
                last.next = node

    # runtime: O(n)
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
        else:
            while last.next:
                if last.next.value == value:
                    last.next = last.next.next
                    break
                last = last.next

    # runtime: O(n)
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
        return last.next