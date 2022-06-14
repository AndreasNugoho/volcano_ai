class Graph:
    def __init__(self):
        self._data = {}
    
    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = []
    
    def vertex(self):
        for key, value in self._data.items():
            print(key, end=' ')
        print()
    
    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].append(y)
            self._data[y].append(x)
    
    def edge(self):
        edges = []
        for key, value in self._data.items():
            for key2 in self._data[key]:
                if key+key2 not in edges and key2+key not in edges:
                    edges.append(key+key2)
        
        for item in edges:
            print(item, end=' ')
        print()
    
    def findPath(self, x, y):
        visited = []
        self.dfs(x, y, visited)
    
    def dfs(self, node, y, visited):
        visited.append(node)
        if node == y:
            print(visited)
        else:
            for item in self._data[node]:
                if item not in visited:
                    self.dfs(item, y, visited)


   
# graph = Graph()
# graph.addVertex('0')
# graph.addVertex('1')
# graph.addVertex('2')
# graph.addVertex('3')
# graph.addVertex('4')
# graph.addVertex('5')
# graph.addVertex('6')
# graph.vertex()
# graph.addEdge('0', '1')
# graph.addEdge('0', '2')
# graph.addEdge('1', '3')
# graph.addEdge('1', '4')
# graph.addEdge('2', '5')
# graph.addEdge('2', '6')
# graph.findPath('0', '6')