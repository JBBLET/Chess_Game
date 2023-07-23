class Player :
    def __init__(self):
        self.__white_side = None
        self.__is_human = None
    
    def get_is_white_side(self):
        return self.__white_side
    
    def get_is_human(self):
        return self.__is_human
    
class Human_player(Player):
    
    def __init__(self,white_side,name):
        super().__init__()
        self.__is_human = True
        self.__white_side = white_side
        self.__name = name

class computer_player(Player):
    
    def __init__(self,white_side):
        super().__init__()
        self.__is_human = False
        self.__white_side = white_side