from spot import Spot
import piecetype

class Board:
    def __init__(self):
        #Initialisation
        self.__board = [[None]*8]*8
        self.reset_board()

    def get_board(self):
        return self.__board

    def reset_board(self):
        #Add the blank spaces
        for i in range(2,7):
            for j in range(8):
                self.__board[i][j] = Spot(i, j, None)

        #add the pawns
        pawn_row = [Spot(1, i, piecetype.Pawn(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_pawn.png')) for i in range(8)]
        pawn_row_black = [Spot(6, i, piecetype.Pawn(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\opawn.png')) for i in range(8)]
        
        #Add the white pieces
        white_row = [Spot(0, 0, piecetype.Rook(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_rook.png')),
                     Spot(0, 1, piecetype.Knight(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_knight.png')),
                     Spot(0, 2, piecetype.Bishops(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_bishop.png')),
                     Spot(0, 3, piecetype.Queen(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_queen.png')),
                     Spot(0, 4, piecetype.King(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_king.png')),
                     Spot(0, 5, piecetype.Bishops(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_bishop.png')),
                     Spot(0, 6, piecetype.Knight(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_knight.png')),
                     Spot(0, 7, piecetype.Rook(True,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\wh_rook.png'))]

        #Add the black pieces
        black_row = [Spot(7, 0, piecetype.Rook(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\orook.png')),
                     Spot(7, 1, piecetype.Knight(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\oknight.png')),
                     Spot(7, 2, piecetype.Bishops(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\obishop.png')),
                     Spot(7, 3, piecetype.Queen(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\oqueen.png')),
                     Spot(7, 4, piecetype.King(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\oking.png')),
                     Spot(7, 5, piecetype.Bishops(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\obishop.png')),
                     Spot(7, 6, piecetype.Knight(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\oknight.png')),
                     Spot(7, 7, piecetype.Rook(False,'F:\Jean-Baptiste\Documents\Projets\Python\Projet\Chess_Game\chess_asset\orook.png'))]
        
        self.__board[0] = white_row
        self.__board[1] = pawn_row
        self.__board[6] = pawn_row_black
        self.__board[7] = black_row

    def get_spot(self,x,y):
        #Return the spot at the coordinates x,y
        try:
            return self.__board[y][x]
        except IndexError:
            print("Index Out of bond")
