# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
#   projects: a, b, c, d, e, f
#   dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
# Output: f, e, a, b, d, c


from treeAndGraph.graph import Graph, Node, Edge
        
            
def buildOrder(projects, dependencies):
    
    projectsLength = len(projects)
    
    graph = Graph([], [])
    for project in projects:
        graph.appendNode(Node(project, []))
    for dependency, project in dependencies:
        node_from = graph.nodeMap[dependency]
        node_to = graph.nodeMap[project]
        graph.appendEdge(Edge(0, node_from, node_to))
        
    order = []
        
    def DFS(node):
        if not node.visited:
            node.visited = True
            node.visiting = True
            for edge in node.edges:
                if edge.node_to.visiting:
                    return False
                DFS(edge.node_to)
            order.append(node.value)
            node.visiting = False
        return True
        
    for node in graph.nodes:
        if DFS(node):
            continue
        break
    
    if len(order) != projectsLength:
        return False
    return order[::-1]


# 2nd method
def buildOrder2(projects, dependencies):
    
    order = []
    
    while len(projects) > 0 :
        seenProjects = {dependency[0] for dependency in dependencies}
        independentProjects = [project for project in projects if project not in seenProjects]
        if len(independentProjects) == 0:
            return False
        order.extend(independentProjects)
        dependencies = [item for item in dependencies if item[1] not in independentProjects]
        projects = [project for project in seenProjects]
    
    return order[::-1]


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

buildOrder(projects, dependencies)