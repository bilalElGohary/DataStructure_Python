class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjList = dict()
        
    # runtime: 
    def __repr__(self):
        graphStr = ""
        for node, neighbors in self.adjList.items():
            graphStr = f"{node} -> {neighbors}.\n"
        return graphStr
            
    
    # runtime: 
    def addNode(self, node):
        if node not in self.adjList:
            self.adjList[node] = set()
        else:
            raise ValueError("Node exists already.")
    
    # runtime: 
    def removeNode(self, node):
        if node not in self.adjList:
            raise ValueError("Node does not exists already.")
        for neighbors in self.adjList.values():
            neighbors.discard(node)
        del self.adjList[node]
    
    # runtime:
    def addEdge(self, fromNode, toNode, weight=None):
        if fromNode not in self.adjList:
            self.addNode(fromNode)
        if toNode not in self.adjList:
            self.addNode(toNode)
        if weight is None:
            self.adjList[fromNode].add(toNode)
            if not self.directed:
                self.adjList[toNode].add(fromNode)
        else:
            self.adjList[fromNode].add((toNode, weight))
            if not self.directed:
                self.adjList[toNode].add((fromNode, weight))

    # runtime:
    def removeEdge(self, fromNode, toNode):
        if fromNode in self.adjList:
            if toNode in self.adjList[fromNode]:
                self.adjList[fromNode].remove(toNode)
            else:
                raise ValueError("Edge does not exists already.")
            if not self.directed:
                if fromNode in self.adjList[toNode]:
                    self.adjList[toNode].remove(fromNode)
        else:
            raise ValueError("Edge does not exists already.")

    # runtime:
    def getNeighbors(self, node):
        return self.adjList.get(node, set())
    
    # runtime:
    def hasNode(self, node):
        return node in self.adjList
    
    # runtime:
    def hasEdge(self, fromNode, toNode):
        if fromNode in self.adjList:
            return toNode in self.adjList[fromNode]
        return False
    
    # runtime:
    def getNodes(self):
        return list(self.adjList.keys())
    
    # runtime:
    def getEdges(self):
        edges = []
        for fromNode, neighbors in self.adjList.items:
            for toNode in neighbors:
                edges.append((fromNode, toNode))
    # runtime: 
    def BFS(self, start):
        visited = set()
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.getNeighbors(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order
    
    # runtime:
    def DFS(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.getNeighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order


if __name__ == "__main__":
    pass
