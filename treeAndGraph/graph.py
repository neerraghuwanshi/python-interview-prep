class Node:
    def __init__(self, value, edges):
        self.value = value
        self.edges = edges
        self.visited = False
        self.visiting = False
        
        
class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.nodeMap = self.makeNodeMap(nodes)
        self.edgeMap = self.makeEdgeMap(edges)
        
    def makeNodeMap(self, nodes):
        nodeMap = {}
        for node in nodes:
            nodeMap[node.value] = node
        return nodeMap
    
    def makeEdgeMap(self, edges):
        edgeMap = {}
        for edge in edges:
            edgeMap[edge.value] = edge
        return edgeMap
        
    def findNodeFromValue(self, value):
        return self.nodeMap[value]

    def appendNode(self, node):
        self.nodes.append(node)
        self.nodeMap[node.value] = node
        if len(node.edges) > 0:
            self.edges.append(node.edges)
        
    def appendEdge(self, edge):
        self.edges.append(edge)
        self.edgeMap[edge.value] = edge
        edge.node_from.edges.append(edge)
    
    def resetVisited(self):
        for node in self.nodes:
            node.visited = False
        
        
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)

# nodes = [
#     node1,
#     node2,
#     node3,
#     node4,
#     node5,
#     node6,
#     node7,
# ]

# edge1 = Edge(1, node1, node2)
# edge2 = Edge(2, node1, node5)
# edge3 = Edge(3, node1, node6)
# edge4 = Edge(4, node1, node7)
# edge5 = Edge(5, node2, node3)
# edge6 = Edge(6, node2, node4)
# edge7 = Edge(7, node4, node1)

# edges = [
#     edge1,
#     edge2,
#     edge3,
#     edge4,
# ]

# graph = Graph(nodes)

# graph.appendEdge(edge1)
# graph.appendEdge(edge2)
# graph.appendEdge(edge3)
# graph.appendEdge(edge4)
# graph.appendEdge(edge5)
# graph.appendEdge(edge6)