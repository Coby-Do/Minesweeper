import random

class Minesweeper_Model():
    # Initialize the model with default values
    def __init__(self):
        self.width = 10
        self.height = 10
        self.bombs = 10
        self.moves = 0
        self.unopenedBombs = 0
        self.gameboard = [[0 for row in range(self.width)] for col in range(self.height)]

    # Reset the gameboard and generate a new game with bombs placed randomly
    def newGame(self):
        self.gameboard = [[0 for row in range(self.width)] for col in range(self.height)]
        self.moves = 0
        self.unopenedBombs = 0

        # Place bombs randomly on the gameboard
        c = 0
        while c < self.bombs:
            row = random.randint(0, self.width - 1)
            col = random.randint(0, self.height - 1)

            if self.gameboard[row][col] != -1:
                c += 1
                self.gameboard[row][col] = -1

        # Calculate the number of bombs in the surrounding cells for each cell
        for row in range(self.width):
            for col in range(self.height):
                if self.gameboard[row][col] == -1:
                    continue

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        newRow, newCol = row + i, col + j
                        if 0 <= newRow < self.width and 0 <= newCol < self.height and self.gameboard[newRow][newCol] == -1:
                            self.gameboard[row][col] += 1

        return self.gameboard

    # Check if the selected cell is a bomb
    def isBomb(self, r, c):
        if self.gameboard[r][c] == -1:
            self.moves += 1
            return True
        else:
            if self.gameboard[r][c] == 0:
                self.unopenedBombs += 1
            self.moves += 1
            return False

    # Returns the current move count
    def getMoveCount(self):
        return self.moves

    # Checks if the player has won the game
    def checkWin(self):
        if self.width * self.height - self.unopenedBombs == self.bombs:
            return True
        else:
            return False
        
    # Recursively reveal empty cells and update the unopenedBombs count
    def revealEmptyCells(self, row, col, visited=None):
        if visited is None:
            visited = set()
        
        # Check if the cell is within the board bounds and not visited
        if 0 <= row < self.width and 0 <= col < self.height and (row, col) not in visited:
            visited.add((row, col))

            # If the cell is empty, reveal its neighbors
            if self.gameboard[row][col] == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        newRow, newCol = row + i, col + j
                        self.revealEmptyCells(newRow, newCol, visited)
            # If the cell has a number, increment the unopenedBombs count
            elif self.gameboard[row][col] > 0:
                self.unopenedBombs += 1
        
        return visited