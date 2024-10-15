from collections import deque

# Define the goal state and the possible moves (up, down, left, right)
goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]  # 0 represents the empty space

# Function to find the position of the empty space (0)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

# Function to make a move by swapping the empty space with its neighbor
def move(state, direction):
    new_state = [row[:] for row in state]
    zero_pos = find_zero(state)
    i, j = zero_pos
    
    if direction == "up" and i > 0:
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    elif direction == "down" and i < 2:
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    elif direction == "left" and j > 0:
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    elif direction == "right" and j < 2:
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    else:
        return None
    
    return new_state

# Function to check if a state is the goal state
def is_goal(state):
    return state == goal_state

# Function to print the puzzle state
def print_state(state):
    for row in state:
        print(row)
    print("\n")

# BFS algorithm
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        print("Exploring state in BFS:")
        print_state(state)  # Print the current state being explored
        
        if is_goal(state):
            return path
        
        visited.add(str(state))
        for direction in ["up", "down", "left", "right"]:
            new_state = move(state, direction)
            if new_state and str(new_state) not in visited:
                queue.append((new_state, path + [direction]))

    return None

# DFS algorithm
def dfs(initial_state):
    stack = [(initial_state, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        print("Exploring state in DFS:")
        print_state(state)  # Print the current state being explored
        
        if is_goal(state):
            return path
        
        visited.add(str(state))
        for direction in ["up", "down", "left", "right"]:
            new_state = move(state, direction)
            if new_state and str(new_state) not in visited:
                stack.append((new_state, path + [direction]))
    
    return None

# Example usage
initial_state = [[1, 2, 3], 
                 [4, 0, 6], 
                 [7, 5, 8]]  # Initial configuration of the 8-puzzle

print("Initial State:")
print_state(initial_state)

# Solve with BFS
print("Solving using BFS:")
bfs_solution = bfs(initial_state)
if bfs_solution:
    print("BFS Solution:", bfs_solution)
else:
    print("No solution found with BFS.")

# Solve with DFS
print("Solving using DFS:")
dfs_solution = dfs(initial_state)
if dfs_solution:
    print("DFS Solution:", dfs_solution)
else:
    print("No solution found with DFS.")

