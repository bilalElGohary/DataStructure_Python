class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
  
  # runtime: O(1)
  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node
    self.size += 1
    return node
  
  # runtime: O(1)
  def pop(self):
    if self.top is None:
      raise ValueError("Stack is Empty")  
    pop = self.top.value
    self.top = self.top.next
    self.size -= 1
    return pop

  # runtime: O(1)
  def peek(self):
    if self.top is None:
      raise ValueError("Stack is Empty")
    return self.top.value
      
  # runtime: O(1)
  def isEmpty(self):
    return self.top is None
  
  # runtime: O(1)
  def __len__(self):
    return self.size
  
  # runtime: O(n)
  def __repr__(self):
    list = []
    current = self.top
    while current is not None:
      list.append(str(current.value))
      current = current.next  
    return "[" + ", ".join(list) + "]"
      
if __name__ == "__name__":
  pass