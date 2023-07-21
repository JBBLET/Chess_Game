import board
import player
import move

class Game:

    def __init__(self,player_1,player_2):
        self.__player = [player_1, player_2]
        self__board = board.Board()
        self.__current_turn = player_1 if player_1.get_is_white() else player_2
        self.__status = "Active"
        self.__moves_played = []

    def make_move(self, player, move):
        selected_piece = move.get_move()