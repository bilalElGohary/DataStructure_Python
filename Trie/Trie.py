class Node:
  def __init__(self):
    self.children = dict()
    self.isEndWord = False
  
class Trie:
  def __init__(self):
    self.root = Node()
  
  # runtime: O(m) - where m is len of the word
  def insert(self, word):
    current = self.root
    for c in word:
      if c not in current.children:
        current.children[c] = Node()
      current = current.children[c]
    current.isEndWord = True
  
  # runtime: O(m)
  def search(self, word):
    current = self.root
    for c in word:
        if c not in current.children:
            return False
        current = current.children[c]
    return current.isEndWord
  
  # runtime: O(m) 
  def delete(self, word):
    self._delete(self.root, word, 0)
  
  # runtime: O(m) 
  def hasPrefix(self, prefix):
    current = self.root
    for c in prefix:
        if c not in current.children:
            return False
        current = current.children[c]
    return True
    

  # runtime: O(m, k) - where m is prefix and k is total num of c
  def startWith(self, prefix):
    words = []
    current = self.root
    for c in prefix:
        if c not in current.children:
            return words
        current = current.children[c]
    def _dfs(current, path):
        if current.isEndWord:
            words.append(''.join(path))
        for c, child in current.children.items():
            _dfs(child, path + [c])
    _dfs(current, list(prefix))
    return words

  # runtime: O(n)
  def listWord(self):
    words = []
    def _dfs(current, path):
        if current.isEndWord:
            words.append(''.join(path))
        for c, child in current.children.items():
            _dfs(child, path + [c])
    _dfs(self.root, [])
    return words


  # helper methods
  def _delete(self, current, word, index):
    if index == len(word):
        if not current.isEndWord:
            return False
        current.isEndWord = False
        return len(current.children) == 0
    c = word[index]
    node = current.children[c]
    if node is None:
        return False
    delCurrent = self._delete(node, word, index+1)
    if delCurrent:
        del current.children[c]
        return len(current.children) == 0 and not current.isEndWord
    return False
    

if __name__ == "__main__":
pass
