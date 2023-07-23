import board
import player
import move

class Game:

    def __init__(self,player_1,player_2):
        self.__player = [player_1, player_2]
        self.__board = board.Board()
        self.__current_turn = player_1 if player_1.get_is_white() else player_2
        self.__status = "Active"
        self.__moves_played = []

    def make_move(self, player, move):

        selected_piece = move.get_piece_moved()
        if selected_piece == None:
            return False
        elif self.__current_turn!=player:
            return False
        elif not(selected_piece.can_move(self.__board,move.get_start(),move.get_end())):
            return False
        else:
            self.__moves_played.append(move)
            move.get_end().set_piece(move.get_start().get_piece())
            move.get_start.set_piece(None)

        if self.__current_turn == self.__player[0]:
            self.__current_turn = self.__player[1]
        else:
            self.__current_turn = self.__player[0]
        return True
                    
