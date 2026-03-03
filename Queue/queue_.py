class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0
  
  # runtime: O(n)
  def __repr__(self):
    item = []
    current = self.front
    while current is not None:
      item.append(str(current.value))
      current = current.next
    return f"[ {", ".join(item)} ]"
  
  # runtime: O(1)
  def __len__(self):
    return self.size
  
  # runtime: O(1)
  def enqueue(self, value):
    node = Node(value)
    if self.rear is None:
      self.rear = self.front = node
    else:
      self.rear.next = node 
      self.rear = node 
    self.size += 1
    
  # runtime: O(1)
  def dequeue(self):
    if self.front is None:
      raise ValueError("The Queue Is Empty.")
    dequeueValue = self.front.value
    self.front = self.front.next
    if self.front is None:
      self.rear = None
    self.size -= 1
    return dequeueValue
  
  # runtime: O(1)
  def peek(self):
    if self.front is None:
      raise ValueError("The Queue Is Empty.")
    return self.front.value
  
  # runtime: O(n)
  def isEmpty(self):
    return self.front is None 