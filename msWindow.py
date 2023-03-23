from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from msModel import * 

# The graphical user interface for Minesweeper Game
class Minesweeper_Window(QMainWindow):

    def __init__(self):
        super(Minesweeper_Window, self).__init__()

        # Variable initializations
        self.width = 10
        self.height = 10
        self.bombs = 10

        # Create a new model for the Minesweeper game
        self.model = Minesweeper_Model()
        self.buttons = []

        # Label to display the number of bombs
        self.bombDisplay = QLabel("10 Bombs")
        font = QFont("Arial", 16, QFont.Bold)
        self.bombDisplay.setFont(font)
        self.bombDisplay.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.bombDisplay.setAlignment(Qt.AlignLeft)

        # Label to display the number of moves taken
        self.moveDisplay = QLabel("Moves: " + str(self.model.moves))
        font = QFont("Arial", 16, QFont.Bold)
        self.moveDisplay.setFont(font)
        self.moveDisplay.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.moveDisplay.setAlignment(Qt.AlignRight)

        # Set up the main widget and layout
        widget = QWidget()
        self.setCentralWidget(widget)
        
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)
        self.layout.addWidget(self.bombDisplay)
        self.layout.addWidget(self.moveDisplay)
        
        # Create the grid of buttons for the Minesweeper game
        self.grid = QGridLayout()

        # Create each button and add it to the layout
        c = -1
        for row in range(self.width):
            for col in range(self.height):
                c += 1
                button = QPushButton()
                button.setObjectName(str(row) + str(col))
                button.clicked.connect(self.buttonClicked)
                self.buttons.append(button)
                self.grid.addWidget(self.buttons[c], row, col)
        self.layout.addLayout(self.grid)
        self.layout.setSpacing(0)

        # Add a menu bar with an option to start a new game
        menu = self.menuBar().addMenu("&Game")
        newAct = QAction("&New", self, shortcut=QKeySequence.New, triggered=self.newGame)
        menu.addAction(newAct)

        self.setWindowTitle("Minesweeper Game")
        self.newGame()

    # Restarts the game and resets the board
    def newGame(self):
        self.bombDisplay.setText("10 Bombs")
        for i in range(len(self.buttons)):
            self.buttons[i].setEnabled(True)
            self.buttons[i].setIcon(QIcon(""))

        self.model.moves = 0
        self.moveDisplay.setText("Moves: " + str(self.model.moves))
        self.model.newGame()

    # Handles button click events and update the game state
    def buttonClicked(self):
        clicked = self.sender()
        userMove = clicked.objectName()
        position = list(userMove)
        r = int(position[0])
        c = int(position[1])

        if self.model.isBomb(r, c) == False:
            revealed_cells = self.model.revealEmptyCells(r, c)
            self.updateButtons(revealed_cells)
            self.moveDisplay.setText("Moves: " + str(self.model.moves))

            if self.model.checkWin():
                self.bombDisplay.setText("You Win")
                for i in range(len(self.buttons)):
                    self.buttons[i].setEnabled(False)
        else:
            self.bombDisplay.setText("Game Over You lose")
            self.moveDisplay.setText("Moves: " + str(self.model.moves))

            for i in range(len(self.buttons)):
                self.buttons[i].setEnabled(False)
                for row in range(self.width):
                    for col in range(self.height):
                        if self.model.gameboard[row][col] == -1:
                            if self.buttons[i].objectName() == (str(row) + str(col)):
                                self.buttons[i].setIcon(QIcon("Minesweeper_bomb.png"))

    # Updates the buttons to reveal game cells
    def updateButtons(self, revealed_cells):
        for r, c in revealed_cells:
            button_name = str(r) + str(c)
            cell_value = self.model.gameboard[r][c]

            for button in self.buttons:
                if button.objectName() == button_name:
                    button.setEnabled(False)

                    if cell_value > 0:
                        icon_file = f"Minesweeper_{cell_value}.png"
                        button.setIcon(QIcon(icon_file))
                    break