import spot
import piece
import piecetype

class Board:
    
    def __init(self):
        #Initialisation
        self.__board = [[]*7]*7
        self.reset_board()

    def reset_board(self):
        #Reset the board
        for i in range(8):
            #add the pawns
            self.__board[i][1] = spot(i, 1, pawn(True))
            self.__board[i][6] = spot(i, 1, pawn(False))
        
        #Add the white pieces
        self.__board[0][0] = spot(0, 0, rook(True))
        self.__board[1][0] = spot(1, 0, knight(True))
        self.__board[2][0] = spot(2, 0, bishop(True))
        self.__board[3][0] = spot(3, 0, queen(True))
        self.__board[4][0] = spot(4, 0, king(True))
        self.__board[5][0] = spot(5, 0, bishop(True))
        self.__board[6][0] = spot(6, 0, knight(True))
        self.__board[7][0] = spot(7, 0, rook(True))

        #Add the black pieces
        self.__board[0][7] = spot(0, 7, rook(False))
        self.__board[1][7] = spot(1, 7, knight(False))
        self.__board[2][7] = spot(2, 7, bishop(False))
        self.__board[3][7] = spot(3, 7, queen(False))
        self.__board[4][7] = spot(4, 7, king(False))
        self.__board[5][7] = spot(5, 7, bishop(False))
        self.__board[6][7] = spot(6, 7, knight(False))
        self.__board[7][7] = spot(7, 7, rook(False))
        
        #Add the blank spaces
        for i in range(2,7,1):
            for j in range(8):
                self.__board[i][j] = spot(i, j, None)

    def get_spot(self,x,y):
        #Return the spot at the coordinates x,y
        try:
            return self.__board[x][y]
        except IndexError:
            print("Index Out of bond")