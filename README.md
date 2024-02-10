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
Depth-First Search (DFS): DFS explores as far as possible along each branch before backtracking. In the project, DFS is implemented using a stack to explore deeper paths first, backtracking when necessary.

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
Breadth-First Search (BFS): BFS explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. BFS is implemented by maintaining a queue of nodes to be explored, and expanding nodes level by level until the goal is found. Run the below commands for awesome visualization of BFS.
```

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

```
```

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

```

# Varying the Cost Function: Uniform Cost Search
UCS explores the node with the lowest cost from the start node. UCS is implemented by exploring nodes solely based on their actual cost from the start node.

```

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

```

# A* Search
A* Search combines the cost to reach the node (g) and the cost to reach the goal (h) to decide the order of exploration. In the project, A* Search is implemented by calculating the total cost for each node and exploring nodes with lower costs first using a priority queue.

```

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

```
