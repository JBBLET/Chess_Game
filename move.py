class Move :
    def __init__(self,player,start,end):
        self.__player = player
        self.__start = start
        self.__end = end
        self.__piece_moved = self.__start.get_piece()

    def get_start(self):
        return self.__start
    
    def get_end(self):
        return self.__end
    
    def get_player(self):
        return self.__player
    
    def get_piece_moved(self):
        return self.__piece_moved