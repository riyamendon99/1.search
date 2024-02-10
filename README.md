# PacQuest: Intelligent Pathfinding for Pacman

Welcome to PacQuest! This repository contains an implementation of intelligent pathfinding algorithms for the classic game Pacman. In this version, 
I've implemented Breadth-First Search (BFS), Depth-First Search (DFS), A* Search, and Uniform Cost Search (UCS) algorithms to help Pacman navigate through the maze and find the optimal path to collect all the food dots.
The base Pacman implementations are developed by the University of California, Berkeley.

## Algorithms Implemented
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search
- Uniform Cost Search (UCS)

## Getting Started
To get started with PacQuest, follow these steps:

1. Clone the repository to your local machine:
   git clone https://github.com/riyamendon99/PacQuest-Intelligent-Pathfinding-for-Pacman.git

2. Navigate to the project directory: cd PacQuest-Intelligent-Pathfinding-for-Pacman

# Finding a Fixed Food Dot using Depth First Search

## Running Pacman on Different Maze Sizes

You can run Pacman on different maze sizes using the following commands:

### Tiny Maze

```

python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs

```

### Medium Maze

```

python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

```

### Big Maze

```

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs

```

# Breadth First Search

```

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

```
```

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

```

# Varying the Cost Function: Uniform Cost Search

```

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

```

# A* Search

```

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

```
