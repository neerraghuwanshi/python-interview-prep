# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.


def findRoute(firstNode, lastNode):
    firstNode.visited = True
    for edge in firstNode.edges:
        if not edge.node_to.visited:
            edge.node_to.visited = True
            if edge.node_to == lastNode or findRoute(edge.node_to, lastNode):
                return True
    return False


def checkNodes(node1, node2):
    stack = node1.edges
    while stack:
        currentEdge = stack.pop()
        currentEdge.node_to.visited = True
        if node2.value == currentEdge.node_to.value:
            return True
        for edge in currentEdge.node_to.edges:
            if edge.node_to.visited != True and edge not in stack:
                stack.append(edge)
    return False
            
                
def RouteBetweenNodes(node1, node2):
    firstCheck = checkNodes(node1, node2)
    if firstCheck:
        return True
    else:
        return checkNodes(node2, node1)