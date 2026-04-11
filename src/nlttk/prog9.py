def display9():
    code = '''import networkx as nx
def simrank(G, c=0.8, iterations=5):
    nodes = list(G.nodes())
    sim = {u: {v: 0 for v in nodes} for u in nodes}
    for n in nodes:
        sim[n][n] = 1
    for _ in range(iterations):
        new_sim = {u: {v: 0 for v in nodes} for u in nodes}
        for u in nodes:
            new_sim[u][u] = 1
            for v in nodes:
                if u == v:
                    continue
                in_u = list(G.predecessors(u))
                in_v = list(G.predecessors(v))
                if len(in_u) == 0 or len(in_v) == 0:
                    new_sim[u][v] = 0
                else:
                    total = 0
                    for i in in_u:
                        for j in in_v:
                            total += sim[i][j]
                    new_sim[u][v] = c * total / (len(in_u) * len(in_v))
        sim = new_sim
    return sim
G = nx.DiGraph()
G.add_edges_from([
    ('A', 'C'),
    ('B', 'C'),
    ('A', 'D'),
    ('B', 'D')
])
result = simrank(G)
print("simRank similarity:\\n")
for u in result:
    for v in result[u]:
        print(f"s({u},{v})={result[u][v]:.2f}")'''
    print(code)
