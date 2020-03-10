class GraphNode(object):
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.visited = False


def dfs(node):
    if not node.visited:
        print(node.label)
        node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)


def bfs(node):
    # store when each node was visited (at what 'level' it was seen)
    level = {node: 0}
    # track which node was visited directly before the current node
    parent = {node: None}
    i = 1
    frontier = [node]
    while frontier:
        # store unvisited notes discovered in this iteration
        next = []
        # current group of nodes to explore
        for u in frontier:
            # check out neighbors of next node in frontier
            for v in u.neighbors:
                # have we seen this one yet?
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    for l in level:
        print(l.label, level[l])
    for p in parent:
        print(p.label)
        if parent[p] is not None:
            print(parent[p].label)


node_a = GraphNode('a')
node_b = GraphNode('b')
node_c = GraphNode('c')
node_d = GraphNode('d')
node_e = GraphNode('e')

node_a.neighbors.add(node_b)
node_a.neighbors.add(node_c)

node_b.neighbors.add(node_a)
node_b.neighbors.add(node_c)
node_b.neighbors.add(node_d)
node_b.neighbors.add(node_e)

node_c.neighbors.add(node_a)
node_c.neighbors.add(node_b)
node_c.neighbors.add(node_d)
node_c.neighbors.add(node_e)

node_d.neighbors.add(node_b)
node_d.neighbors.add(node_c)
node_d.neighbors.add(node_e)

node_e.neighbors.add(node_b)
node_e.neighbors.add(node_c)
node_e.neighbors.add(node_d)

graph = [node_a, node_b, node_c, node_d, node_e]

bfs(node_a)

