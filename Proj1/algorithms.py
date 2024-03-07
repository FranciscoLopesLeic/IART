from collections import deque
import heapq
from gamelogic import *


# TreeNode modelo
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

        

def breadth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)   # create the root node in the search tree
    queue = deque([root])   # initialize the queue to store the nodes
    
    while queue:
        node = queue.popleft()   # get first element in the queue
        if goal_state_func(node.state):   # check goal state
            return node
        
        for state in operators_func(node.state):   # go through next states
            # create tree node with the new state
            newNode = TreeNode(state)
            
            # link child node to its parent in the tree
            node.add_child(newNode)
            
            # enqueue the child node
            queue.append(newNode)
            

    return



def depth_first_search(initial_state,goal_state_func,operators_func):
    root = TreeNode(initial_state)
    result = depth_first_search_rec(root,goal_state_func,operators_func,[])
    if(result != None):
        return result
    return None

def depth_first_search_rec(node, goal_state_func, operators_func, state_list):
    if(goal_state_func(node.state)):  # create the root node in the search tree
        return node
      
    state_list.append(node.state)
    for state in operators_func(node.state):
        if(state not in state_list):
            # create tree node with the new state
            newNode = TreeNode(state)

            node.add_child(newNode)

            result = depth_first_search_rec(newNode,goal_state_func,operators_func,state_list)
            if(result != None):
                return result
    return None




def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
    root = TreeNode(initial_state)
    result = depth_limited_search_rec(root,goal_state_func,operators_func,[],depth_limit,0)
    if(result != None):
        return result
    return None

def depth_limited_search_rec(node, goal_state_func, operators_func, state_list,depth_limit,current_depth):
    if(goal_state_func(node.state)):  # create the root node in the search tree
        return node
    if current_depth == depth_limit:
        return None
      
    state_list.append(node.state)
    for state in operators_func(node.state):
        if(state not in state_list):
            # create tree node with the new state
            newNode = TreeNode(state)

            node.add_child(newNode)

            result = depth_limited_search_rec(newNode,goal_state_func,operators_func,state_list,depth_limit,current_depth+1)
            if(result != None):
                return result
    return None



def iterative_deepening_search(initial_state, goal_state_func, operators_func, depth_limit):
    depth_limit = 0
    while True:
        result = depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit)
        if result is not None:
            return result
        depth_limit += 1




def bfs(problem):
    # problem(NPuzzleState) - the initial state
    queue = [problem]
    visited = set() # to not visit the same state twice

    while queue:
        x=0
        # ...
        # ...
        # TO COMPLETE
        # ...
        # ...
    return None




def greedy_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    # Mudar o NPuzzle
    setattr(Cogito, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice
    current_state = problem
    heap_states = []

    while states:
        if current_state.is_complete():
            return current_state.move_history
        visited.add(current_state)
        children_states = current_state.children()
        for c_state in children_states:
            heapq.heappush(heap_states,c_state)
            
        next_state = heapq.heappop(heap_states)

        while next_state in visited:
            if not heap_states:  # If no unvisited neighbors, break out of loop
                next_state = None
                break
            next_state = heapq.heappop(heap_states)

        
        current_state = next_state
            
        # TO COMPLETE
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        # ...
        # ...
        
    return None

def _preferential_position(number, side):
    # calculates the preferred position of a piece given its number
    # number (int) - the number of the piece
    # side (int) - the size of the side of the board (only for square boards)
    if number == 0:
        # if it is the last piece, it is 0
        row = col = side - 1
    else:
        # otherwise it is sequential, starting at 1
        row = number // side
        col = number % side - 1
    return (row, col)

def h1(state):
    # heuristic function 1
    # returns the number of incorrect placed pieces in the matrix
    board = state.board
    side = len(board) # the size of the side of the board (only for square boards)

    total = 0
    
    # checks if the board is complete
    for row in range(len(board)):
        for col in range(len(board[0])):
            (desired_row,desired_col) = _preferential_position(board[row][col],len(board))
            if row != desired_row or desired_col != col:
                total += 1
    return total

def h2(state):
    # heuristic function 2
    # returns the sum of manhattan distances from incorrect placed pieces to their correct places
    board = state.board
    side = len(board) # the size of the side of the board (only for square boards)

    total = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            (desired_row,desired_col) = _preferential_position(board[row][col],len(board))
            total += abs(col-desired_col) + abs(row-desired_row)
    return total