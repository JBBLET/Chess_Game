import board
import numpy as np

class Piece : 
    def __init__(self,white=False,name=None,img=None):
        self.__is_white = white
        self.__is_killed = False
        self.__name = name
        self.__image = img
    
    def is_white(self):
        return self.__is_white

    def is_killed(self):
        return self.__is_killed
    
    def set_killed(self,killed):
        self.__is_killed = killed

    def set_white(self,white):
        self.__is_white = white

    def can_move(self,board,start,end):
        #return if a move is legal
        return False
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_image(self):
        return self.__image
    
class Pawn(Piece):
    def __init__(self,white,image):
        super().__init__(white,"Pawn",img=image)
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
        elif dif_x == 1 and dif_y == 1 and end.get_piece().is_white() != self.is_white():
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
    def __init__(self,white,image):
        super().__init__(white,"Bishops",img=image)

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
        #
        start_pos_X, start_pos_Y = start.get_pos_X(), start.get_pos_Y()
        end_pos_X, end_pos_Y = end.get_pos_X(), end.get_pos_X()

        if start_pos_X==end_pos_X:
            dir_X=0
        else:
            dir_X=(end_pos_X-start_pos_X)//(abs(end_pos_X-start_pos_X))
        if start_pos_Y==end_pos_Y:
            dir_Y=0
        else:
            dir_Y=(end_pos_Y-start_pos_Y)//(abs(end_pos_Y-start_pos_Y))

        checked_spot_coord = [start_pos_X+dir_X,start_pos_Y+dir_Y]

        while  checked_spot_coord != [end_pos_X, end_pos_Y]:
            checked_spot= board.get_spot(checked_spot_coord[0],checked_spot_coord[1])
            if checked_spot.get_piece()!=None:
                print("There is a piece in between in :({},{})".format(checked_spot_coord[0],checked_spot_coord[1]))
                return False
            
            checked_spot_coord[0] += dir_X
            checked_spot_coord[1] += dir_Y
        return True
    
class Knight(Piece):
    def __init__(self,white,image):
        super().__init__(white,"Knight",img=image)

    def can_move(self,board,start,end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        return (dif_x*dif_y == 2)
    
class Rook(Piece):
    def __init__(self,white,image):
        super().__init__(white,"Rook",img=image)
        self.__already_moved = False

    def get_already_moved(self):
        return self.__already_moved
    
    def set_already_moved(self, moved):
        self.__already_moved = moved

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
        #
        start_pos_X, start_pos_Y = start.get_pos_X(), start.get_pos_Y()
        end_pos_X, end_pos_Y = end.get_pos_X(), end.get_pos_X()

        if start_pos_X==end_pos_X:
            dir_X=0
        else:
            dir_X=(end_pos_X-start_pos_X)//(abs(end_pos_X-start_pos_X))
        if start_pos_Y==end_pos_Y:
            dir_Y=0
        else:
            dir_Y=(end_pos_Y-start_pos_Y)//(abs(end_pos_Y-start_pos_Y))

        checked_spot_coord = [start_pos_X+dir_X,start_pos_Y+dir_Y]

        while  checked_spot_coord != [end_pos_X, end_pos_Y]:

            checked_spot = board.get_spot(checked_spot_coord[0],checked_spot_coord[1])
            if checked_spot.get_piece()!=None:
                print("There is a piece in between in :({},{})".format(checked_spot_coord[0],checked_spot_coord[1]))
                return False
            
            checked_spot_coord[0] += dir_X
            checked_spot_coord[1] += dir_Y
        return True

class Queen(Piece):
    def __init__(self,white,image):
        super().__init__(white,"Queen",img=image)

    def can_move(self,board,start,end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        if dif_x*dif_y != 0 and dif_x!=dif_y:
            return False
        else:
            return(self.no_piece_in_between(board,start,end))
    
    def no_piece_in_between(self,board,start,end):

        start_pos_X, start_pos_Y = start.get_pos_X(), start.get_pos_Y()
        end_pos_X, end_pos_Y = end.get_pos_X(), end.get_pos_X()

        if start_pos_X==end_pos_X:
            dir_X=0
        else:
            dir_X=(end_pos_X-start_pos_X)//(abs(end_pos_X-start_pos_X))
        if start_pos_Y==end_pos_Y:
            dir_Y=0
        else:
            dir_Y=(end_pos_Y-start_pos_Y)//(abs(end_pos_Y-start_pos_Y))

        checked_spot_coord = [start_pos_X+dir_X,start_pos_Y+dir_Y]
        while  checked_spot_coord != [end_pos_X, end_pos_Y]:
            checked_spot = board.get_spot(checked_spot_coord[0],checked_spot_coord[1])
            if checked_spot.get_piece()!=None:
                print("There is a piece in between in :({},{})".format(checked_spot_coord[0],checked_spot_coord[1]))
                return False
            
            checked_spot_coord[0] += dir_X
            checked_spot_coord[1] += dir_Y
        return True
    
class King(Piece):
    def __init__(self,white,image):
        super().__init__(white,"King",img=image)
        self.__already_castle =False

    def get_already_castle(self):
        return self.__already_castle
    
    def set_already_castle(self,castle):
        self.__already_castle = castle

    def can_move(self,board, start, end):
        #We can't move to where a same color piece is
        if end.get_piece().is_white() == self.is_white():
            return False
        
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())
        
        if dif_x+dif_y == 1 or dif_x*dif_y == 1:
            return self.king_not_under_attack(board,end)
        else:
            return(self.is_valid_castle(board,start,end))
    
    def king_not_under_attack(self,board,end):
        board_matrix = board.get_board()
        for row in board_matrix:
            for spot in row:
                if spot!=end:
                    if spot.get_piece().is_white()!=self.is_white() and spot.get_piece().can_move(board,spot,end):
                        return False
        return True

    def is_valid_castle(self,board,start,end):
        #
        start_pos_X, end_pos_X = start.get_pos_X(), end.get_pos_X()
        dif_x , dif_y = abs(start.get_pos_X()-end.get_pos_X()), abs(start.get_pos_Y()-end.get_pos_Y())

        if dif_y!=0 or dif_x!=2:
            return False
        
        else:
            dir_X=(end_pos_X-start_pos_X)//(abs(end_pos_X-start_pos_X))
            checked_spot_coord = start_pos_X+dir_X

            while checked_spot_coord!=end_pos_X:
                checked_spot = board.get_spot(checked_spot_coord, start.get_pos_Y())
                if checked_spot.get_piece()!=None or checked_spot.get_piece().get_name()!="Rook":
                    return False
                elif not(self.king_not_under_attack(board,checked_spot)):
                    return False
                
            rook_pos = int((1+dir_X)*3.5)
            rook = board.get_spot(rook_pos, start.get_pos_Y()).get_piece()
            if rook.get_piece().get_name() != "Rook" or rook.get_piece().get_already_moved():
                return False
            else:
                return True 
