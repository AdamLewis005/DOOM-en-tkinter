from mainwindow import MainWindow
from game import Game
from player import Player

import tkinter as tk

#initialise ce qui a besoin pour commencer le jeu
  
player = Player(45.1,45.1,"red")
game = Game(player)
main = MainWindow(game)
img = tk.PhotoImage(file="Bottons.png")
win= tk.PhotoImage(file="doom.ppm")
game.promp = img
game.win = win
game.status_bar = main.status_bar
game.canvas = main.canvas
main.mainloop()
