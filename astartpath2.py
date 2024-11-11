import pygame  # type: ignore
import heapq
import sys

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Final path (now green)
RED = (255, 0, 0)    # Start
BLUE = (0, 0, 255)   # Goal
YELLOW = (255, 255, 0)  # Open nodes
PURPLE = (128, 0, 128)  # Closed nodes

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def astar(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {node: float('inf') for node in grid}
    g_score[start] = 0

    f_score = {node: float('inf') for node in grid}
    f_score[start] = heuristic(start, goal)

    open_nodes = set()
    closed_nodes = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current), open_nodes, closed_nodes

        open_nodes.add(current)
        closed_nodes.add(current)

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in open_nodes and neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, open_nodes, closed_nodes

def get_neighbors(node, grid):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor = (node[0] + dx, node[1] + dy)
        if neighbor in grid and grid[neighbor] == 0:  # 0 = walkable
            neighbors.append(neighbor)
    return neighbors

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def draw_grid(screen, grid, path, player_pos, goal, open_nodes, closed_nodes):
    for x in range(ROWS):
        for y in range(COLS):
            color = WHITE if grid[(x, y)] == 0 else BLACK  # Walkable or blocked
            pygame.draw.rect(screen, color, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    # Draw open nodes
    for (x, y) in open_nodes:
        pygame.draw.rect(screen, YELLOW, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    # Draw closed nodes
    for (x, y) in closed_nodes:
        pygame.draw.rect(screen, PURPLE, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    # Draw the final path in green
    if path:
        for (x, y) in path:
            pygame.draw.rect(screen, GREEN, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    # Draw start and goal
    pygame.draw.rect(screen, RED, (player_pos[1] * GRID_SIZE, player_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)  # Start
    pygame.draw.rect(screen, BLUE, (goal[1] * GRID_SIZE, goal[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)  # Goal

    # Draw grid lines
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Create a grid with walkable (0) and blocked (1) cells
    grid = {(x, y): 0 for x in range(ROWS) for y in range(COLS)}

    # Set initial player position and goal
    player_pos = (0, 0)  # Starting position
    goal = (10, 10)      # Goal position
    path = []

    running = True
    algorithm_running = False  # Flag to track if the algorithm is running
    open_nodes, closed_nodes = set(), set()  # Initialize sets for open and closed nodes

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid[(y // GRID_SIZE, x // GRID_SIZE)] = 1 if grid[(y // GRID_SIZE, x // GRID_SIZE)] == 0 else 0
                
                # Set goal point with left click
                if event.button == 1:  # Left click
                    goal = (y // GRID_SIZE, x // GRID_SIZE)

                # Set start point with right click
                elif event.button == 3:  # Right click
                    player_pos = (y // GRID_SIZE, x // GRID_SIZE)

                # Start the A* algorithm
                if player_pos != goal:  # Only start if player and goal are different
                    path, open_nodes, closed_nodes = astar(player_pos, goal, grid)  # Run the A* algorithm
                    algorithm_running = True  # Start the algorithm

            # Allow the user to reset the grid by pressing 'R'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset grid
                    grid = {(x, y): 0 for x in range(ROWS) for y in range(COLS)}
                    player_pos = (0, 0)  # Reset start position
                    goal = (10, 10)      # Reset goal position
                    path = []            # Reset path
                    algorithm_running = False  # Stop the algorithm
                    open_nodes, closed_nodes = set(), set()  # Reset open and closed nodes

        # Run the A* pathfinding
        if algorithm_running:
            path, open_nodes, closed_nodes = astar(player_pos, goal, grid)

        screen.fill(WHITE)
        draw_grid(screen, grid, path, player_pos, goal, open_nodes, closed_nodes)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
