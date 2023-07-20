import board.py
import numpy as np
class Piece : 
    def __init__(self,x,y,couleur,board=None):
        self.__couleur = couleur
        self.__position = np.array((x,y))
        self.__moves= []
        if self.__couleur=='blanc':
            self.__direction=-1
        else:
            self.__direction=+1
        self.__value = 0
        self.__board = board


    def getPosition(self):
        return (self.__position)
    
    def setPostion(self,x,y):
        self.__position = np.array(x,y)
    
    def getMoves(self):
        return self.__movesLegal
    
    def setBoard(self,board):
        self.__board = board
