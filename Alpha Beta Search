MAX = float('inf')
MIN = float('-inf')

def minmax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminal node (leaf of the game tree)
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN  # Initialize the best value for maximizing player
        
        # Recur for the two children of the current node
        for i in range(2):  # Assuming binary tree with two children
            val = minmax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)  # Choose the maximum value
            alpha = max(alpha, best)  # Update alpha

            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        
        return best
    
    else:
        best = MAX  # Initialize the best value for minimizing player
        
        # Recur for the two children of the current node
        for i in range(2):  # Assuming binary tree with two children
            val = minmax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)  # Choose the minimum value
            beta = min(beta, best)  # Update beta

            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        
        return best

# Example usage
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
    print("The optimal value is:", minmax(0, 0, True, values, MIN, MAX))
