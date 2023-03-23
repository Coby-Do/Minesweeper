from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from msWindow import *

# This is the main application, all it does is set up a Qt application,
# tell it to show our msWindow, and then let Qt take over

app = QApplication([])
window = Minesweeper_Window()
window.show()
app.exec_()