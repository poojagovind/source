There are a total of n classes labeled with the English alphabet (A, B, C, and so on). Some classes are dependent on other classes for compilation. For example, if class B extends class A, then B has a dependency on A. Therefore,A must be compiled before B.
Given a list of the dependency pairs, find the order in which the classes should be compiled.

def find_compilation_order(dependencies):
    sorted_order = []
    graph = {}
    inDegree = {}
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        inDegree[parent], inDegree[child] = 0, 0
    if len(graph) <= 0:
        return sorted_order


    for dependency in dependencies:
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)  
        inDegree[child] += 1  

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]: 
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if len(sorted_order) != len(graph):
        return []
    return sorted_order