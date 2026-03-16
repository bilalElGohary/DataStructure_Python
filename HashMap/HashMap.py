class hashMap:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.buckets = [[] for _ in range(capacity)]
  
  # runtime: O(1)
  def __len__(self):
    return self.size
  
  # runtime: O(n), O(1)
  def __contains__(self, key):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k == key:
        return True
    return False
    
  # runtime: O(n), O(1)
  def get(self, key):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k == key:
        return v
    raise KeyError("Key Not Found.")
  
  # runtime: O(1), O(1)
  def put(self, key, value):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        bucket[i] = (key, value)
      else:
        bucket.append((key, value))
    self.size += 1
  
  # runtime: O(n), O(1)
  def remove(self, key):
    index = self._hash_func(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        del bucket[i]
        self.size -= 1
        break
    else:
      raise KeyError("Key Not Found.")

  # runtime: O(n)
  def keys(self):
    return [k for bucket in self.buckets for k, _ in bucket]
  
  # runtime: O(n)
  def values(self):
    return [v for bucket in self.buckets for _, v in bucket]

  # runtime: O(n)
  def item(self):
    return [(k, v) for bucket in self.buckets for k, v in bucket]
  
  def _hash_func(self, key):
    keyStr = str(key)
    hashRes  = 0
    for c in keyStr:
      hashRes = (hashRes * 31 + ord(c)) % self.capacity
    return hashRes