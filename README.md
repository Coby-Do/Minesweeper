# Minesweeper

Minesweeper is a classic single-player puzzle game where the objective is to clear a rectangular grid containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. This implementation of Minesweeper uses the Model-View-Controller (MVC) design pattern to ensure separation of concerns between the game logic, user interface, and control flow.

## Languages Used:

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Features

- 10x10 grid with 10 hidden mines
- Clues provided for the number of neighboring mines
- Recursive revealing of empty cells upon clicking a cell with no neighboring mines
- Move counter to track the number of moves taken
- Win detection when all non-mine cells have been revealed
- Bomb display showing the total number of bombs on the grid
- Game over detection when a mine is clicked
- Ability to start a new game at any time
- Built using PyQt5 for a visually appealing and responsive user interface

## Getting Started

To run the Minesweeper game, you will need to have Python 3 and PyQt5 installed on your system. You can install PyQt5 using the following command:

```bash
pip install PyQt5
```

After installing the required dependencies, simply run the minesweeper.py file to start the game:

```bash
python msMain.py
```

## How to Play

1. Start a new game by clicking "Game" in the menu bar and selecting "New" or by pressing **Ctrl+N**.
2. Click on any cell in the 10x10 grid to reveal its content. If it's a mine, the game is over, and all mines will be displayed.
3. If the revealed cell is not a mine, it will show a number indicating the count of neighboring mines. Use this information to deduce the locations of mines.
4. Continue revealing cells until all non-mine cells have been uncovered. When this occurs, you win the game!

## Here's an image of the gameboard

<img width="247" alt="image" src="https://user-images.githubusercontent.com/111834642/227373742-4ca34393-65e6-4461-96d4-3ecc2ed6d8db.png">

## Model-View-Controller Design Pattern

This Minesweeper implementation follows the Model-View-Controller (MVC) design pattern, which separates the application into three interconnected components:

- Model (**msModel.py**): Represents the game logic, including the Minesweeper board state, handling moves, checking for wins, and revealing empty cells.
- View (**msMain.py**, **msWindow** class): Represents the user interface, including the grid of buttons, move counter, bomb display, and menu bar.
- Controller (**msMain.py**, event handling functions): Handles user input, such as button clicks, and communicates between the model and view to update the game state and display.

By following the MVC design pattern, the code is organized, modular, and easy to maintain or extend with new features.

## License

This project is licensed under the MIT License. Feel free to use, modify, or distribute the code as needed.

## Acknowledgements

- Thanks to the developers of **PyQt5** for providing an excellent framework for creating the graphical user interface.
- Special thanks to the Minesweeper community for continuing to enjoy and support this classic gam
