class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjList = dict()
        
    # runtime: 
    def __repr__(self):
        pass
    
    # runtime: 
    def addNode(self, node):
        pass
    
    # runtime: 
    def removeNode(self, node):
        pass
    
    # runtime:
    def addEdge(self, fromNode, toNode, weight=None):
        pass
    
    # runtime:
    def removeEdge(self, fromNode, toNode):
        pass
    
    # runtime:
    def getNeighbors(self, node):
        pass
    
    # runtime:
    def hasNode(self, node):
        pass
    
    # runtime:
    def hasEdge(self, fromNode, toNode):
        pass
    
    # runtime:
    def getNodes(self):
        pass
    
    # runtime:
    def getEdges(self):
        pass

if __name__ == "__main__":
    pass
