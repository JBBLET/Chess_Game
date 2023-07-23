import spot
import piecetype

class Board:
    
    def __init(self):
        #Initialisation
        self.__board = [[]*7]*7
        self.reset_board()

    def get_board(self):
        return self.__board
    
    def reset_board(self):
        #Reset the board
        for i in range(8):
            #add the pawns
            self.__board[i][1] = spot(i, 1, piecetype.pawn(True))
            self.__board[i][6] = spot(i, 1, piecetype.pawn(False))
        
        #Add the white pieces
        self.__board[0][0] = spot(0, 0, piecetype.rook(True))
        self.__board[1][0] = spot(1, 0, piecetype.knight(True))
        self.__board[2][0] = spot(2, 0, piecetype.bishop(True))
        self.__board[3][0] = spot(3, 0, piecetype.queen(True))
        self.__board[4][0] = spot(4, 0, piecetype.king(True))
        self.__board[5][0] = spot(5, 0, piecetype.bishop(True))
        self.__board[6][0] = spot(6, 0, piecetype.knight(True))
        self.__board[7][0] = spot(7, 0, piecetype.rook(True))

        #Add the black pieces
        self.__board[0][7] = spot(0, 7, piecetype.rook(False))
        self.__board[1][7] = spot(1, 7, piecetype.knight(False))
        self.__board[2][7] = spot(2, 7, piecetype.bishop(False))
        self.__board[3][7] = spot(3, 7, piecetype.queen(False))
        self.__board[4][7] = spot(4, 7, piecetype.king(False))
        self.__board[5][7] = spot(5, 7, piecetype.bishop(False))
        self.__board[6][7] = spot(6, 7, piecetype.knight(False))
        self.__board[7][7] = spot(7, 7, piecetype.rook(False))
        
        #Add the blank spaces
        for i in range(2,7,1):
            for j in range(8):
                self.__board[i][j] = spot.Spot(i, j, None)

    def get_spot(self,x,y):
        #Return the spot at the coordinates x,y
        try:
            return self.__board[x][y]
        except IndexError:
            print("Index Out of bond")
