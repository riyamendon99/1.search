# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""
    
    
    """print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    "*** YOUR CODE HERE ***"
    """
    closed = set() # a set to capture the visited nodes
    pathStack = Stack()
    direction = []
    closed.add(problem.getStartState())
    pathStack.push((problem.getStartState(),direction)) #initially appending the node to visited set and to Stack

    while (pathStack.isEmpty() == False):
        coordinates, direction = pathStack.pop() #pop each element to process its successors

        for c in problem.getSuccessors(coordinates):
            if c[0] not in closed:
                closed.add(c[0]) #Adding the child nodes to visited set so that they are not processed again
                pathStack.push((c[0], direction + [c[1]])) #push the child nodes on top of stack
                
        if problem.isGoalState(coordinates):
            return direction

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    closed = set()
    pathQueue = Queue() #taking queue here as data structure since we need to search at each level and then increment
    closed.add(problem.getStartState())
    pathQueue.push((problem.getStartState(), []))

    while pathQueue.isEmpty() == False:
        coordinates, direction = pathQueue.pop()
        if (problem.isGoalState(coordinates)): #check if goal node is reached or not
            return direction

        for c in problem.getSuccessors(coordinates):
            if c[0] not in closed:
                closed.add(c[0]) #adding explored nodes in a set
                pathQueue.push((c[0], direction + [c[1]])) #adding the new action to the existing actions
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set() # a set to store all the visited nodes
    direction = []
    pathPriorityQueue = PriorityQueue() #taking a priortiy queue to pull out the least cost
    pathPriorityQueue.push((problem.getStartState(), direction), 0) #the cost from root node to itself is 0
    visited.add(problem.getStartState())

    while pathPriorityQueue.isEmpty() == False:
        coordinates, direction = pathPriorityQueue.pop()

        for c in problem.getSuccessors(coordinates):
            if c[0] not in visited:
                totalCost = problem.getCostOfActions(direction + [c[1]])
                pathPriorityQueue.push((c[0], direction + [c[1]]), totalCost) #adding cost of the existing path cost
                visited.add(c[0])

        if problem.isGoalState(coordinates):
            return direction
        
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    direction = []
    pathPriorityQueueA = PriorityQueue() #priority queue for pulling out least cost
    pathPriorityQueueA.push((problem.getStartState(), direction), heuristic) #initial cost is 0
    visited.add(problem.getStartState())

    while pathPriorityQueueA.isEmpty() == False:
        coordinates, direction = pathPriorityQueueA.pop()

        for c in problem.getSuccessors(coordinates):
            if c[0] not in visited:
                #totalCost = problem.getCostOfActions(direction + [c[1]]) + heuristic(c[0], problem) #adding cost of path to the heuristic cost
                pathPriorityQueueA.push((c[0], direction + [c[1]]), heuristic)
                visited.add(c[0])

        if problem.isGoalState(coordinates):
            return direction
    
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
