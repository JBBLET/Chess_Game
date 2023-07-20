import piece.py
import board.py
import numpy as np

class Pawn(Piece):

    def __init__(self,white):
        super().__init__(white)
        self.__already_moved = False

    def get_already_moved(self):
        return self.__already_moved
    
    def set_already_moved(self,already_moved):
        self.__already_moved = already_moved

    def can_move(self, board, start, end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        if dif_x == 0 and dif_y == 1 and end.get_piece() == None:
            return True
        elif dif_x == 1 and dif_y == 1 and end.get_piece().is_white() == not(self.is_white()):
            return True
        elif dif_x == 0 and dif_y == 2:
            return(self.is_valid_first_move(board,start,end))
        else:
            return False
        
    def is_valid_first_move(self,board,start,end):
        if self.__already_moved:
            return False
        middle_spot = board.get_spot(end.get_pos_X(),(start.get_pos_Y()+end.get_pos_Y())//2)
        if middle_spot.get_piece()==None:
            return True

class Bishops(Piece):
    def __init__(self,white):
        super().__init__(white)

    def can_move(self,board,start,end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        if dif_x!=dif_y:
            return False
        else:
            return(self.no_piece_in_between(board,start,end))
        
    def no_piece_in_between(self,board,start,end):
        start_pos_X, start_pos_Y = start.get_pos_X(), start.get_pos_Y()
        end_pos_X, end_pos_Y = end.get_pos_X(), end.get_pos_X()
        if start_pos_X<=end_pos_X:
            dir_X=1
        else:
            dir_X=-1
        if start_pos_Y<=end_pos_Y:
            dir_Y=1
        else:
            dir_Y=-1
        checked_spot_X, checked_spot_Y = start_pos_X+dir_X,start_pos_Y+dir_Y
        while  checked_spot_X!=end_pos_X:
            checked_spot = board.get_spot(checked_spot_X,checked_spot_Y)
            if checked_spot.get_piece()!=None:
                print("There is a piece in between in :({},{})".format(checked_spot_X,checked_spot_Y))
                return False
        return True
    
class Knight(piece):
    def __init__(self,white):
        super().__init__(white)

    def can_move(self,board,start,end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        return (dif_x*dif_y == 2)
    
class Rook(piece):
    def __init__(self,white):
        super().__init__(white)

    def can_move(self,board,start,end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        if dif_x*dif_y != 0:
            return False
        else:
            return(self.no_piece_in_between(board,start,end))
    
    def no_piece_in_between(self,board,start,end):
        start_pos_X, start_pos_Y = start.get_pos_X(), start.get_pos_Y()
        end_pos_X, end_pos_Y = end.get_pos_X(), end.get_pos_X()
        if start_pos_X<=end_pos_X:
            dir_X=1
        else:
            dir_X=-1
        if start_pos_Y<=end_pos_Y:
            dir_Y=1
        else:
            dir_Y=-1
        checked_spot_X, checked_spot_Y = start_pos_X+dir_X,start_pos_Y+dir_Y
        while  checked_spot_X!=end_pos_X:
            checked_spot = board.get_spot(checked_spot_X,checked_spot_Y)
            if checked_spot.get_piece()!=None:
                print("There is a piece in between in :({},{})".format(checked_spot_X,checked_spot_Y))
                return False
        return True