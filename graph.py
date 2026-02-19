from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()

def construct_path(parent, start, end):
    path = [end]
    curr = end
    while curr != start:
        curr = parent[curr]
        path.append(curr)
    return path[::-1]

#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False
def BFS2(G, node1, node2):
    if node1 == node2:
        return [node1]
    Q = deque([node1])
    parent = {node1: None}
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                parent[node] = current_node 
                return construct_path(parent, node1, node2)
            if node not in parent:
                parent[node] = current_node
                Q.append(node)

    return []
def BFS3(G, node1):
    Q = deque([node1])
    predecessors = {}
    marked = {node1}

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node not in marked:
                marked.add(node)           
                predecessors[node] = current_node 
                Q.append(node)
                
    return predecessors

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False
def DFS2(G, node1, node2):
    if node1 == node2:
        return [node1]
    S = [(node1, None)]
    parent = {} 
    while len(S) != 0:
        current_node, predecessor = S.pop()
        if current_node not in parent:
            parent[current_node] = predecessor
            if current_node == node2:
                return construct_path(parent, node1, node2)
            for neighbor in G.adj[current_node]:
                if neighbor not in parent:
                    S.append((neighbor, current_node))
    
    return []
def DFS3(G, node1):
    S = [(node1, None)]
    predecessors = {}
    marked = set()
    while len(S) != 0:
        current_node, parent = S.pop() 
        if current_node not in marked:
            marked.add(current_node)
            if parent is not None:
                predecessors[current_node] = parent
            for neighbor in G.adj[current_node]:
                if neighbor not in marked:
                    S.append((neighbor, current_node))
                    
    return predecessors

#is connected
def is_connected(G):
    if len(G.adj) == 0:
        return True
    start_node = list(G.adj.keys())[0]
    reachable_nodes = BFS3(G, start_node)
    if len(reachable_nodes) + 1 == len(G.adj):
        return True
    else:
        return False
    
#has cycle
def has_cycle(G):
    visited = set()
    for start_node in G.adj:
        if start_node not in visited:
            stack = [(start_node, -1)]
            while len(stack) > 0:
                current, parent = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                for neighbor in G.adj[current]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return True
                    stack.append((neighbor, current))

    return False

#Use the methods below to determine minimum vertex covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


