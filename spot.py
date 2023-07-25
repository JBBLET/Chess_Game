class Spot:
    #A spot represents one of the place of the 8x8 grid
    def __init__(self, x, y, piece):
        self.__piece = piece
        self.__pos_X = x
        self.__pos_Y = y
    
    def get_piece(self):
        return self.__piece
    
    def set_piece(self,piece):
        self.__piece = piece

    def get_pos_X(self):
        return self.__pos_X
    
    def get_pos_Y(self):
        return self.__pos_Y

    def set_pos_X(self,x):
        self.__pos_X = x

    def set_pos_Y(self,y):
        self.__pos_Y = y
    
    def __str__(self) -> str:
        return("("+str(self.__pos_X)+","+str(self.__pos_Y)+")")
