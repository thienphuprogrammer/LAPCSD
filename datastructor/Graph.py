class EdgeNode:
    def __init__(self, v, cost):
        self.v = v
        self.cost = cost


class AdjacencyGraph:
    def __init__(self):
        self.__numVertices = 0  # number of vertices in the graph
        self.__mapVertices = {}  # dictionary mapping vertices to edges

    def getNumVertices(self):
        return self.__numVertices

    def getNumEdges(self):
        numEdges = 0
        for v in self.__mapVertices:
            numEdges += len(self.__mapVertices[v])
        return numEdges

    def getAllVertices(self):
        return self.__mapVertices

    def addVertex(self, v: int):
        if self.__mapVertices.get(v) is None:
            self.__mapVertices[v] = []
            self.__numVertices += 1

    def addEdge(self, fr: int, to: int, cost=0):
        if fr not in self.__mapVertices:
            self.addVertex(fr)
        if to not in self.__mapVertices:
            self.addVertex(to)
        for v in self.__mapVertices[fr]:
            if v.v == to:
                raise Exception("Edge already exists")
        self.__mapVertices[fr].append(EdgeNode(to, cost))

    def updateEdge(self, fr: int, to: int, cost=0):
        if fr not in self.__mapVertices or to not in self.__mapVertices:
            raise Exception("Vertex does not exist")
        for v in self.__mapVertices[fr]:
            if v.v == to:
                v.w = cost
                return
        raise Exception("Edge does not exist")

    def getEdges(self):
        edges = []
        for v in self.__mapVertices:
            for e in self.__mapVertices[v]:
                edges.append((v, e.v, e.w))
        return edges

    def getCost(self, fr: int, to: int):
        for v in self.__mapVertices[fr]:
            if v.v == to:
                return v.cost
        raise Exception("Edge does not exist")

    def __DFS(self, fr: int, to: int, visited: dict, path: list, paths: list, cost):
        visited[fr] = True
        path.append(fr)
        if fr == to:
            paths.append({
                "path": path.copy(),
                "cost": cost
            })
        else:
            for v in self.__mapVertices[fr]:
                if not visited[v.v]:
                    self.__DFS(v.v, to, visited, path, paths, cost + v.cost)
        path.pop()
        visited[fr] = False

    def getAllPaths(self, fr: int, to: int):
        visited = {}
        for v in self.__mapVertices:
            visited[v] = False
        path = []
        paths = []
        if fr not in self.__mapVertices or to not in self.__mapVertices:
            raise Exception("Vertex does not exist")

        self.__DFS(fr, to, visited, path, paths, 0)
        return paths

    def deleteVertex(self, v: int):
        if v not in self.__mapVertices:
            raise Exception("Vertex does not exist")
        del self.__mapVertices[v]
        for key in self.__mapVertices:
            for i in range(len(self.__mapVertices[key])):
                if self.__mapVertices[key][i].v == v:
                    del self.__mapVertices[key][i]
                    break

    def deleteEdge(self, fr, to):
        if fr not in self.__mapVertices or to not in self.__mapVertices:
            raise Exception("Vertex does not exist")
        for i in range(len(self.__mapVertices[fr])):
            if self.__mapVertices[fr][i].v == to:
                del self.__mapVertices[fr][i]
                return
        raise Exception("Edge does not exist")

# G = AdjacencyGraph()
# G.addVertex(0)
# G.addVertex(1)
# G.addVertex(2)
# G.addVertex(3)
# G.addVertex(6)
# G.addEdge(0, 1, 1)
# G.addEdge(0, 2, 1)
# G.addEdge(0, 3, 1)
# G.addEdge(1, 0, 1)
# G.addEdge(1, 3, 1)
# G.addEdge(2, 0, 1)
# G.addEdge(2, 3, 1)
# G.addEdge(3, 0, 1)
# G.addEdge(3, 1, 1)
# G.addEdge(3, 2, 1)
# G.addEdge(3, 4, 1)
# G.addEdge(4, 3, 1)
# G.addEdge(0, 4, 1)
# G.addEdge(4, 0, 1)
# G.addEdge(4, 2, 1)
# G.addEdge(2, 4, 1)
# G.getAllVertices()
# G.deleteVertex(4)
# print('After delete vertex 4')
# G.getAllVertices()
# print('All paths from 0 to 6')
# print(G.getAllPaths(0, 6))
