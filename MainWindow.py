import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal
from PyQt5.QtGui import QDrag, QPixmap
from game import Game  
from player import *
from move import Move

class Case(QLabel):
    clicked = pyqtSignal(int, int)

    def __init__(self, piece, row, col, parent=None):
        super().__init__(piece, parent)
        self.piece = piece
        self.row = row
        self.col = col

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.row, self.col)

class ChessboardWidget(QWidget):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initUI()
        self.queue = []

    def initUI(self):
        self.grid_layout = QGridLayout()
        self.setStyleSheet("background-color: white;")
        self.grid_layout.setSpacing(0)
        self.setLayout(self.grid_layout)
        self.updateChessboard()

    def updateChessboard(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            self.grid_layout.removeWidget(widget)

        size = min(self.width(), self.height())
        grid_size = 8
        cell_size = size / grid_size

        board = self.game.get_board().get_board()
        for row in range(grid_size):
            for col in range(grid_size):
                spot = board[row][col]
                if spot.get_piece() != None:
                    chess_piece = Case(spot.get_piece().get_name(), row, col)
                    chess_piece.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    chess_piece.setStyleSheet(" border: 2px solid black; background-color: #F0D9B5;" if (row + col) % 2 == 0 else "border: 2px solid black; background-color: #B58863;")
                    self.pixmap = QPixmap(spot.get_piece().get_image())
                    chess_piece.setPixmap(self.pixmap)
                    chess_piece.setScaledContents(True)
                    chess_piece.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))
                    chess_piece.clicked.connect(self.onCaseClicked)
                    self.grid_layout.addWidget(chess_piece, row, col)
                else:
                    case = Case('',row,col)
                    case.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    case.setStyleSheet("border: 2px solid black; background-color: #F0D9B5;" if (row + col) % 2 == 0 else "border: 2px solid black; background-color: #B58863;")
                    case.clicked.connect(self.onCaseClicked)
                    self.grid_layout.addWidget(case, row, col)

                
    def onCaseClicked(self, row, col):
        print("Clicked on case:", row, col)
        self.queue.append([row,col])
        if (row,col) == self.queue[-1]:
            self.queue.pop()
        if len(self.queue) == 2:
            end = self.queue.pop()
            start = self.queue.pop()
            end = self.game.get_board().get_spot(end[0],end[1])
            start = self.game.get_board().get_spot(start[0],start[1])
            move = Move(self.game.get_current(),start,end)
            print(move)
            print(self.game.make_move(self.game.get_current(),move))
        self.updateChessboard()
       
    
    def resizeEvent(self, event):
        self.updateChessboard()


class MoveHistoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create a label for the header
        header_label = QLabel("Move History")
        layout.addWidget(header_label)

        # Create labels to display moves (you can add actual moves here)
        move_labels = [QLabel(f"Move {i+1}") for i in range(5)]  # Example: showing 5 moves
        for move_label in move_labels:
            layout.addWidget(move_label)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initUI()

    def initUI(self):
        central_widget = QWidget()

        # Create ChessboardWidget and MoveHistoryWidget
        chessboard_widget = ChessboardWidget(self.game)
        move_history_widget = MoveHistoryWidget()

        # Create layout for the main window
        main_layout = QHBoxLayout()
        main_layout.addWidget(chessboard_widget)
        main_layout.addWidget(move_history_widget)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Set the window properties
        self.setWindowTitle("Chessboard GUI Example")
        self.setGeometry(100, 100, 800, 400)


    def resizeEvent(self, event):
        # Call resizeEvent of the parent class to handle its resizing
        super().resizeEvent(event)
        self.centralWidget().findChild(ChessboardWidget).updateChessboard()
        self.centralWidget().findChild(MoveHistoryWidget).update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player1 = Human_player(True,'player1')
    player2 = Human_player(False,'player2')
    game = Game(player1,player2)  # Initialize your Game class here
    window = MainWindow(game)   
    window.show()
    sys.exit(app.exec_())