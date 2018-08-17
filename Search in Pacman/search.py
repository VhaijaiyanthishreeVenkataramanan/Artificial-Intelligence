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
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"
    # We are utilizing the stack data structure from util.py
    child = util.Stack()

    #In order to write the graph search version of DFS, we are utilizing set() which avoids duplicates
    #by not visiting a node more than once

    expanded = set()

    #To begin with, we push the start state coordinates and empty list of directions on to the child

    child.push((problem.getStartState(), [], 0))

    #Runs the loop until the child is empty
    while not child.isEmpty():
        state, actions, cost = child.pop()

    #Check if the popped node and goal state are same and if yes, return the list of actions for pacman to reach goal
        if problem.isGoalState(state):
            return actions
    #If node is already visited, do not push its successors onto the child
        if state in expanded:
            continue
    #if the node is not visited, mark it as visited and push its successors onto the child
        expanded.add(state)
        for next_state, next_action, next_cost in problem.getSuccessors(state):
            child.push((next_state, actions + [next_action], next_cost))

    return []

""" Result statictics for a tiny maze: Path found with total cost of 10 in 0.0 seconds
Search nodes expanded: 15
Pacman emerges victorious! Score: 500
Average Score: 500.0
Scores:        500.0
Win Rate:      1/1 (1.00)
Record:        Win

Result statictics for a medium maze: Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 146
Pacman emerges victorious! Score: 380
Average Score: 380.0
Scores:        380.0
Win Rate:      1/1 (1.00)
Record:        Win

Result statictics for a big maze: Path found with total cost of 210 in 0.0 seconds
Search nodes expanded: 390
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win
"""


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    # We are utilizing the queue data structure from util.py
    child = util.Queue()

    # In order to write the graph search version of BFS, we are utilizing set() which avoids duplicates
    #by not visiting a node more than once
    expanded = set()

    # To begin with, we push the start state coordinates and empty list of directions on to the child
    child.push((problem.getStartState(), [], 0))

    # Runs the loop until the child is empty
    while not child.isEmpty():
        state, actions, cost = child.pop()

        # Check if the popped node and goal state are same and if yes, return the list of actions for pacman to reach goal
        if problem.isGoalState(state):
            return actions

        # If node is already visited, do not push its successors onto the child
        if state in expanded:
            continue
        # if the node is not visited, mark it as visited and push its successors onto the child
        expanded.add(state)
        for next_state, next_action, next_cost in problem.getSuccessors(state):
            child.push((next_state, actions + [next_action], next_cost))

    return []

"""Result statstics for a medium maze: Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0
Scores:        442.0
Win Rate:      1/1 (1.00)
Record:        Win

Result statictics for a big maze: Path found with total cost of 210 in 0.1 seconds
Search nodes expanded: 620
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win
"""



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # We are utilizing the priority queue data structure from util.py
    child = util.PriorityQueue()

    # In order to write the graph search version of BFS, we are utilizing set() which avoids duplicates
    #by not visiting a node more than once
    expanded = set()

    #Cost matters in UCS. So it is passed as 0 for initial state and priority as 0
    # To begin with, we push the start state coordinates, empty list of directions, cost and priority on to the child
    child.push((problem.getStartState(), [], 0), 0)

    # Runs the loop until the child is empty
    while not child.isEmpty():
        state, actions, cost =  child.pop()

        # Check if the popped node and goal state are same and if yes, return the list of actions for pacman to reach goal
        if problem.isGoalState(state):
            return actions

        # If node is already visited, do not push its successors onto the child
        if state in expanded:
            continue
        # if the node is not visited, mark it as visited and push its successors onto the child
        expanded.add(state)
        for next_state, next_action, next_cost in problem.getSuccessors(state):
            child.push((next_state, actions + [next_action], cost + next_cost), cost + next_cost)

    return []

"""Result statstics for a medium maze: Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0
Scores:        442.0
Win Rate:      1/1 (1.00)
Record:        Win

Result statstics for a medium dotted maze: Path found with total cost of 1 in 0.0 seconds
Search nodes expanded: 186
Pacman emerges victorious! Score: 646
Average Score: 646.0
Scores:        646.0
Win Rate:      1/1 (1.00)
Record:        Win

Result statstics for a medium scary maze: Path found with total cost of 68719479864 in 0.0 seconds
Search nodes expanded: 108
Pacman emerges victorious! Score: 418
Average Score: 418.0
Scores:        418.0
Win Rate:      1/1 (1.00)
Record:        Win
"""

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # We are utilizing the priority queue data structure from util.py
    child = util.PriorityQueue()

    # In order to write the graph search version of BFS, we are utilizing set() which avoids duplicates
    # by not visiting a node more than once
    expanded = set()

    # Cost matters in Astar. So it is passed as 0 for initial state and priority as 0(cost) + heuristic of start state
    # To begin with, we push the start state coordinates, empty list of directions, cost and priority on to the child
    child.push((problem.getStartState(), [], 0), 0 +heuristic(problem.getStartState(), problem))

    # Runs the loop until the child is empty
    while not child.isEmpty():
        state, actions, cost = child.pop()

        # Check if the popped node and goal state are same and if yes, return the list of actions for pacman to reach goal
        if problem.isGoalState(state):
            return actions

        # If node is already visited, do not push its successors onto the child
        if state in expanded:
            continue
        # if the node is not visited, mark it as visited and push its successors onto the child
        expanded.add(state)
        for next_state, next_action, next_cost in problem.getSuccessors(state):
            child.push((next_state, actions + [next_action], cost + next_cost), cost + next_cost + heuristic(next_state, problem))

    return []

"""Result statstics for a big maze: Path found with total cost of 210 in 0.0 seconds
Search nodes expanded: 549
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win
"""


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

