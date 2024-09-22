def hill_climbing_min_cost(cost):
    n = len(cost)
    
    # Edge cases: no steps or only one step
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    # Initialize an array to store the minimum cost to reach each step
    cost_from_start = [float('inf')] * n
    cost_from_start[0] = cost[0]
    cost_from_start[1] = cost[1]
    
    # Iterate through the cost array
    for i in range(n):
        # Update the cost for the next step (i + 1)
        if i + 1 < n:
            cost_from_start[i + 1] = min(cost_from_start[i + 1], cost_from_start[i] + cost[i + 1])
        # Update the cost for the step after next (i + 2)
        if i + 2 < n:
            cost_from_start[i + 2] = min(cost_from_start[i + 2], cost_from_start[i] + cost[i + 2])

    # Return the minimum cost to reach either the last or second-last step
    return min(cost_from_start[n - 1], cost_from_start[n - 2])

# Example usage
cost = [10, 15, 20]
print(hill_climbing_min_cost(cost))
