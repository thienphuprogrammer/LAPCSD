class EdgeNode:
    def __init__(self, v, w):
        self.v = v
        self.w = w


class AdjacencyGraph:
    def __init__(self, numVertices=0):
        self.numVertices = numVertices  # number of vertices in the graph
        self.mapVertices = {}  # dictionary mapping vertices to edges

    def updateVertex(self, u, v, w):
        if self.mapVertices.get(u) is None:
            self.mapVertices[u] = []
            self.mapVertices[u].append(EdgeNode(v, w))
        else:
            for item in self.mapVertices[u]:
                if item.v == v:
                    item.w = w
                    break
            else:
                self.mapVertices[u].append(EdgeNode(v, w))

    def addVertex(self, u, v, w=0):
        if self.mapVertices.get(u) is None:
            self.mapVertices[u] = []
            self.mapVertices[u].append(EdgeNode(v, w))
        else:
            self.mapVertices[u].append(EdgeNode(v, w))

        self.numVertices += 1

    def getVertex(self):
        return self.mapVertices.keys()

    def getEdges(self):
        edges = []
        for v in self.mapVertices:
            for e in self.mapVertices[v]:
                edges.append((v, e.v, e.w))
        return edges


G = AdjacencyGraph(5)
G.addVertex("ALG", "ATL", 1)
G.addVertex("ALG", "ORD", 2)
G.addVertex("ATL", "ALG", 1)
G.addVertex("ATL", "ORD", 1)
G.addVertex("ATL", "LAX", 2)
G.addVertex("ORD", "ALG", 2)
G.addVertex("ORD", "ATL", 1)
G.addVertex("ORD", "LAX", 2)
G.addVertex("LAX", "ATL", 2)
G.addVertex("LAX", "ORD", 2)
print("Vertices of graph:", G.getVertex())
for key, value in G.mapVertices.items():
    print(key, end=": ")
    for i in value:
        print("{v:", i.v, ",w:", i.w, "}, ", end=" ")

    print()
