# Development of an Optimized Pathfinding Algorithm for Video Games

This project focuses on the development of a high-performance, optimized pathfinding algorithm tailored for video game environments. It combines efficient search techniques and practical optimizations to achieve smooth and responsive character navigation, even in complex terrains or with dynamic obstacles.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [User Interaction](#user-interaction)
- [Technical Approach](#technical-approach)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Future Work](#future-work)
- [License](#license)

## Overview
Pathfinding in video games requires a blend of speed, accuracy, and adaptability. This project explores various pathfinding algorithms, enhancing them to suit real-time game requirements. The optimized algorithm can handle dynamic obstacles, dense grids, and provides visual feedback for algorithm steps.

## Features
- **Optimized Pathfinding**: Designed for rapid calculations in grid-based video game maps.
- **Real-Time Obstacle Detection**: Adjusts the path dynamically when obstacles appear or disappear.
- **Algorithm Visualization**: See each step as the algorithm progresses in real-time.
- **Maze and Terrain Generation**: Provides random mazes to test the pathfinding capabilities.
  
## User Interaction
- **Right Click**: Remove start, end, or wall cell and revert it to a normal cell.
- **Left Click**: Set a normal cell as a wall cell.
- **Buttons**:
  - Select a pathfinding algorithm.
  - Clear the grid.
  - Generate a random maze.

> **Note**: After removing a start or end cell with right-click, reinstate it by left-clicking on any cell before running the algorithm.

## Technical Approach
### Algorithms Implemented
1. **Optimized Dijkstra's Algorithm**
2. **Enhanced A* Search Algorithm**
3. **Bidirectional Search**
4. **Breadth-First Search (BFS)**
5. **Depth-First Search (DFS)**


### Optimized Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest path between nodes in a weighted graph. This implementation optimizes the algorithm with a priority queue, making it efficient for dense graphs.

### Enhanced A* Search Algorithm
The A* algorithm improves search efficiency by using a heuristic function to guide the path search. This version uses an optimized heuristic function for faster convergence.

### Bidirectional Search
Bidirectional search reduces search time by simultaneously searching from both the start and end nodes, meeting in the middle.

### Breadth-First Search (BFS)
BFS is ideal for unweighted graphs, finding the shortest path by exploring each node layer-by-layer.

### Depth-First Search (DFS)
DFS explores each branch of the graph as far as possible before backtracking. It’s useful for checking connectivity and detecting cycles.

## Applications
- **Network Routing**: Dijkstra’s and A* for optimal paths.
- **Pathfinding in Games**: A* for real-time decision-making.
- **Social Networks**: BFS for level-based exploration (e.g., degree of separation).
- **Cycle Detection**: DFS to detect cycles in dependency graphs.

## Complexity
| Algorithm                  | Time Complexity | Space Complexity | Best For                         |
|----------------------------|-----------------|------------------|----------------------------------|
| Optimized Dijkstra's       | \(O((V + E) \log V)\) | \(O(V + E)\) | Weighted shortest path          |
| Enhanced A* Search         | \(O((V + E) \log V)\) | \(O(V + E)\) | Heuristic-based shortest path   |
| Bidirectional Search       | \(O(b^{d/2})\) | \(O(b^{d/2})\)  | Large undirected graphs         |
| Breadth-First Search (BFS) | \(O(V + E)\)   | \(O(V)\)        | Unweighted shortest path        |
| Depth-First Search (DFS)   | \(O(V + E)\)   | \(O(V)\)        | Connectivity and cycle checking |

## Installation
Clone this repository and run the `GraphSearch` class to see each algorithm in action.

## Usage
```bash
```
Install dependencies:
```bash
pip install pygame
