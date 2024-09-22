def breadth_first_search(graph, start): 
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize the queue with the start node
    visited.add(start)  # Mark the start node as visited

    while queue: 
        node = queue.pop(0)  # Dequeue a node
        print(node)  # Perform an action on the node (currently printing)

        # Loop through the neighbors of the current node
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor
    
    return visited  # Return all visited nodes

# Define the graph as a dictionary
graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'F'], 
    'D': ['B'], 
    'E': ['B', 'F'], 
    'F': ['C', 'E'] 
}

# Start BFS from node 'A'
start_node = 'A' 
visited_nodes = breadth_first_search(graph, start_node)
