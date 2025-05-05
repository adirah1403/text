# Taking graph input from the user
graph = {}

# Number of vertices (nodes)
n = int(input("Enter the number of vertices: "))

# Taking edges input
for _ in range(n):
    vertex = int(input("\nEnter the vertex: "))
    graph[vertex] = []  # Initialize empty list
    num_neighbors = int(input("Enter number of neighbors of vertex " + str(vertex) + ": "))
    
    for _ in range(num_neighbors):
        neighbor = int(input("Enter neighbor: "))
        graph[vertex].append(neighbor)

# Set to track visited nodes
visited = set()

# Recursive DFS function
def dfs(vertex):
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(neighbor)

# Start DFS from a starting vertex
start_vertex = int(input("\nEnter the starting vertex for DFS: "))
print("\nDFS Traversal:")
dfs(start_vertex)
