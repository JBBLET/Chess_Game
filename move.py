class Move :
    def __init__(self,player,start,end):
        self.__player = player
        self.__start = start
        self.__end = end
        self.__piece_moved = self.__start.get_piece()

    