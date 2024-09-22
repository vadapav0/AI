import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = 0  # g(n)
        self.heuristic = 0  # h(n)
        self.total = 0  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.total < other.total

def goal_state(size):
    # Generates the goal state for the puzzle based on the size
    return tuple(tuple((i * size + j + 1) % (size * size) for j in range(size)) for i in range(size))

# Define the goal and start states
goal = goal_state(3)  # 3x3 puzzle
start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

def manhattan_heuristic(state, goal):
    # Calculate the Manhattan distance heuristic
    size = len(state)
    distance = 0
    for i in range(size):
        for j in range(size):
            if state[i][j] != 0:  # Exclude the empty space (0)
                x, y = divmod(state[i][j] - 1, size)
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(node):
    # Get neighboring states by moving the blank (0) tile
    neighbors = []
    size = len(node.state)
    x, y = [(ix, iy) for ix, row in enumerate(node.state) for iy, i in enumerate(row) if i == 0][0]  # Find the empty space (0)
    directions = {'Up': (x - 1, y), 'Down': (x + 1, y), 'Left': (x, y - 1), 'Right': (x, y + 1)}

    for move, (new_x, new_y) in directions.items():
        if 0 <= new_x < size and 0 <= new_y < size:  # Check if move is within bounds
            new_state = [list(row) for row in node.state]  # Create a copy of the state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]  # Swap the blank with the neighboring tile
            neighbors.append(PuzzleNode(tuple(tuple(row) for row in new_state), node, move, node.depth + 1))

    return neighbors

def reconstruct_puzzle_path(node):
    # Reconstruct the path from the goal to the start
    path = []
    while node:
        path.append((node.move, node.state))
        node = node.parent
    return path[::-1]  # Reverse to get the path from start to goal

def astar_puzzle(start, goal):
    # A* algorithm to solve the 8-puzzle problem
    open_list = []
    closed_set = set()
    start_node = PuzzleNode(start)
    goal_node = goal
    start_node.heuristic = manhattan_heuristic(start, goal_node)
    start_node.total = start_node.heuristic
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        # If the goal is reached, return the solution path
        if current_node.state == goal_node:
            return reconstruct_puzzle_path(current_node)

        closed_set.add(current_node.state)

        # Explore the neighbors of the current node
        for neighbor in get_neighbors(current_node):
            if neighbor.state in closed_set:
                continue

            neighbor.cost = current_node.depth + 1
            neighbor.heuristic = manhattan_heuristic(neighbor.state, goal_node)
            neighbor.total = neighbor.cost + neighbor.heuristic

            heapq.heappush(open_list, neighbor)

    return None  # No solution found

# Run the A* algorithm on the start state and print the solution path
solution = astar_puzzle(start_state, goal)
if solution:
    for move, state in solution:
        print(f"Move: {move}")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
