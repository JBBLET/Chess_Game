import piece.py
import board.py
import numpy as np

class Pawn(Piece):

    def __init__(self,x,y,couleur,board):
        super().__init__(x,y,couleur,board)
        self.__firstmove == True
        if self.__couleur == 'black':
            self.__direction = np.array([(0,-1)])
        else : 
            self.__direction = np.array([(0,1)])
        self.__value = 1

    def setMoves(self,Board): 
        moves = []
        if self.__firstmove:
            moves.append(self.__position + self.__direction)
            moves.append(self.__position + 2*self.__direction)
        else:
            moves.append(self.__position + self.__direction)
        if Board[self.__position[0]+self.__direction[1],self.__postion[1]+1].getCouleur != self.__couleur :
            moves.append((self.__position[0]+self.__direction[1],self.__postion[1]+1))
        if Board[self.__position[0]+self.__direction[1],self.__postion[1]-1].getCouleur != self.__couleur :
            moves.append((self.__position[0]+self.__direction[1],self.__postion[1]-1))
        self.__moves= moves
