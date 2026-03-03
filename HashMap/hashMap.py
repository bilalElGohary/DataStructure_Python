class hashMap:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.buckets = [[] for _ in range(capacity)]
  
  # runtime: O(1)
  def __len__(self):
    return self.size
  
  # runtime: O(n)
  def __contains__(self, key):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k == key:
        return True
    return False
    
  # runtime: O(n)
  def get(self, key, value):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k == key:
        return v
    raise KeyError("Key Not Found.")
  
  def put(self, key):
    pass
  
  def remove(self, key):
    pass
  
  def keys(self):
    pass
  
  def values(self):
    pass
  
  def item(self):
    pass
  
  def _hash_func(self, key):
    keyStr = str(key)
    hashRes  = 0
    for c in keyStr:
      hashRes = (hashRes * 31 + orc(c)) % self.capacity