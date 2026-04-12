def display11():
    code = '''from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
g = Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
print("Following is Breadth First Traversal (starting from vertex 2):")
g.BFS(2)'''
    print(code)
