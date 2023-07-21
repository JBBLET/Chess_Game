import board.py
import numpy as np

class Piece : 
    def __init__(self,white=False,name=None):
        self.__is_white = white
        self.__is_killed = False
        self.__name = name

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