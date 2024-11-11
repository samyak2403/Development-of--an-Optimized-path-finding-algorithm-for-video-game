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

### Key Optimizations
- **Heuristics**: A* search algorithm with an optimized heuristic for video game maps.
- **Dynamic Obstacle Handling**: Real-time path recalculations.
- **Memory Management**: Efficient data structures for larger grids.

## Requirements
- **Languages**: Python
- **Libraries**:
  - `pygame` for visualization
  - `heapq` for priority queue management
  - `random` for maze generation
  - `time` for performance tracking

Install dependencies:
```bash
pip install pygame
