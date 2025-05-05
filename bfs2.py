from collections import deque

# Taking graph input from the user
graph = {}

n = int(input("Enter the number of vertices: "))

for _ in range(n):
    vertex = int(input("\nEnter the vertex: "))
    graph[vertex] = []
    num_neighbors = int(input("Enter number of neighbors of vertex " + str(vertex) + ": "))
    
    for _ in range(num_neighbors):
        neighbor = int(input("Enter neighbor: "))
        graph[vertex].append(neighbor)

# Set to track visited nodes
visited = set()

# BFS function
def bfs(start):
    queue = deque()
    queue.append(start)
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)   
                queue.append(neighbor)

# Start BFS
start_vertex = int(input("\nEnter the starting vertex for BFS: "))
print("\nBFS Traversal:")
bfs(start_vertex)
