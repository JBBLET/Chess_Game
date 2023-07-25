from board import Board
import player
import move

class Game:
    def __init__(self,player_1,player_2):
        self.__player = [player_1, player_2]
        self.__board_game = Board()
        self.__current_turn = player_1 if player_1.get_is_white_side() else player_2
        self.__status = "Active"
        self.__moves_played = []

    def get_current(self):
        return self.__current_turn
    
    def get_board(self):
        return self.__board_game
    
    def make_move(self, player, move):
        selected_piece = move.get_piece_moved()
        if selected_piece == None:
            print("here")
            return False
        elif self.__current_turn!=player:
            print("ici")
            return False
        elif not(selected_piece.can_move(self.__board_game,move.get_start(),move.get_end())):
            print("la")
            return False
        else:
            self.__moves_played.append(move)
            move.get_end().set_piece(move.get_start().get_piece())
            move.get_start().set_piece(None)

        if self.__current_turn == self.__player[0]:
            self.__current_turn = self.__player[1]
        else:
            self.__current_turn = self.__player[0]
        return True
                    
