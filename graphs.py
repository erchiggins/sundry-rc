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

dfs(node_a)
