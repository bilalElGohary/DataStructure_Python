class MinHeap:
  def __init__(self):
    self.heap = []
    
  def __len__(self):
    return len(self.heap)
    
  def __repr__(self):
    return str(self.heap)
    
  # runtime: O(log n) 
  def insert(self, key, value):
    self.heap.append((key, value))
    self._siftUp(len(self.heap) - 1)
  
  # runtime: O(1)
  def peekMin(self):
    if not self.heap:
      raise IndexError("The heap is empty.")
    return self.heap[0]
  
  # runtime: O(log n)
  def extractMin(self):
    if not self.heap:
      raise IndexError("The heap is empty.")
    min = self.heap[0]
    last = self.heap.pop()
    if self.heap:
      self.heap[0] = last
      self._siftDown(0)
    return min
  
  # runtime: O(n)
  def heapify(self, elements):
    self.heap = list(elements)
    for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
      self._siftDown(i)
  
  # runtime: O(n)
  def meld(self, otherHeap):
    combined = self.heap + otherHeap
    self.heapify(combined)
    otherHeap.heap = []
  
  # helper methods
  def _parent(self, index):
    return (index + 1) // 2 if index != 0 else None
  
  def _left(self, index):
    left = 2 * index + 1
    return left if left < len(self.heap) else None
  
  def _right(self, index):
    right = 2 * index + 2
    return right if right < len(self.heap) else None

  
  def _siftUp(self, index):
    # swim
    parent = self._parent(index)
    while parent is not None and self.heap[index][0] < self.heap[parent][0]:
      self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
      index = parent
      parent = self._parent(index)
  
  def _siftDown(self, index):
    # sink
    while True:
      smallest = index
      left = self._left
      right = self._right
      if left is not None and self.heap[left][0] < self.heap[smallest][0]:
        smallest = left
      if right is not None and self.heap[right][0] < self.heap[smallest][0]:
        smallest = right
      if smallest == index:
        break
    self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
    index = smallest

    
if __name__ == "__main__":
  pass
