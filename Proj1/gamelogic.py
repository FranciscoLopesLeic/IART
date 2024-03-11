from enum import Enum
import numpy as np
 
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Line(Enum):
    ROW = 1
    COLUMN = 2

class Cogito:
    def __init__(self,board,final_board):
        #Note: board must be quadratic (len(row)==len(column))
        self.board = board
        self.final_board = final_board
        self.size = len(board)

    def check_win(self):
        if self.board == self.final_board:
            return True
        else:
            return False
        

    '''needed for the visited list'''
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        
    def get_moves(self):
        moves = []
        
        for i in range(0,len(self.board)):
            board_up = self.move(Direction.UP,Line.COLUMN,i)
            board_down = self.move(Direction.DOWN,Line.COLUMN,i)
            board_right = self.move(Direction.RIGHT,Line.ROW,i)
            board_left = self.move(Direction.LEFT,Line.ROW,i)
            moves.append(Cogito(board_up,self.final_board))
            moves.append(Cogito(board_down,self.final_board))
            moves.append(Cogito(board_right,self.final_board))
            moves.append(Cogito(board_left,self.final_board))
        return moves
                


    def move(self,direction,line,n):
        # DIRECTION MUST BE UP,DOWN,LEFT,RIGHT
        # LINE can be row or column
        # n is the number of the line to move
        

        # Validate the input
        # UP and DOWN needs Column and LEFT and RIGHT needs Row
        if not (((direction == Direction.UP or direction == Direction.DOWN) and line==Line.COLUMN) or ((direction == Direction.LEFT or direction == Direction.RIGHT) and line==Line.ROW)):
            return None
        if n >= len(self.board):
            return None
        
        # Proceeds to change the board
        old_board = self.board
        new_board = np.zeros((len(old_board),len(old_board[0]))).astype(int)
        
        # FOR LOOP - rows
        if(line == Line.ROW):
            for row in range(len(old_board)):
                for column in range(len(old_board[row])):
                    if n == row:
                        if direction == Direction.RIGHT:
                            new_board[row][column] = old_board[row][column-1]
                        elif direction == Direction.LEFT:
                            if column == len(old_board[row])-1:
                                new_board[row][column] = old_board[row][0]
                            else:
                                new_board[row][column] = old_board[row][column+1]
                        else:
                            new_board[row][column] = old_board[row][column]
                    else:
                        new_board[row][column] = old_board[row][column]

        # FOR LOOP - Columns
        elif line == Line.COLUMN:
            for row in range(len(old_board)):
                for column in range(len(old_board[row])):
                    if n == column:
                        if direction == Direction.UP:
                            if row == len(old_board)-1:
                                new_board[row][column] = old_board[0][column]
                            else:
                                new_board[row][column] = old_board[row+1][column]
                        elif direction == Direction.DOWN:
                            if row == 0:
                                new_board[row][column] = old_board[len(old_board[0])-1][column]
                            else:
                                new_board[row][column] = old_board[row-1][column]
                        else:
                            new_board[row][column] = old_board[row][column]
                    else:
                        new_board[row][column] = old_board[row][column]
        #Maybe define new board as board.
        return new_board
    
    def __hash__(self):
        # to be able to use the state in a set
        return hash(str([item for sublist in self.board for item in sublist]))

    def __eq__(self, other):
        # compares the two matrices
        return [item for sublist in self.board for item in sublist] == [item for sublist in other.board for item in sublist]
    def __str__(self):
        return str(np.matrix(self.board))
    

def check_win(self):
    if (np.array(self.board) == np.array(self.final_board)).all():
        return True
    else:
        return False

def get_moves(self):
        moves = []
        
        for i in range(0,len(self.board)):
            board_up = self.move(Direction.UP,Line.COLUMN,i)
            board_down = self.move(Direction.DOWN,Line.COLUMN,i)
            board_right = self.move(Direction.RIGHT,Line.ROW,i)
            board_left = self.move(Direction.LEFT,Line.ROW,i)
            moves.append(Cogito(board_up,self.final_board))
            moves.append(Cogito(board_down,self.final_board))
            moves.append(Cogito(board_right,self.final_board))
            moves.append(Cogito(board_left,self.final_board))
        return moves
