import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import sys
from menu import Menu
from canvas import Canvas
from game import Game
from statusbar import StatusBar
class MainWindow:
    """Fenetre principale"""
    def __init__(self,game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Le Fake du fake de DOOM")
        self.root.protocol("WM_DELETE_WINDOW", self.quit) #bouton x 
        self.status_bar = StatusBar(self.root)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.menu = Menu(self.root,self.game)
        self.canvas = Canvas(self.game,self.root, width=800, height=600,bg = "grey")
        self.canvas.pack(padx="2m", pady="2m")
        self.root.bind('a',self.canvas.move_player_left)
        #self.root.bind('q',self.canvas.move_player_left)
        self.root.bind('d',self.canvas.move_player_right)
        self.root.bind('w',self.canvas.move_player_up)
        self.root.bind('z',self.canvas.move_player_up)
        self.root.bind('s',self.canvas.move_player_down)
        self.root.bind('k',self.canvas.rotate_player_left)
        self.root.bind('l',self.canvas.rotate_player_right)
        self.root.bind("<Escape>",self.esc)
        self.start_button = tk.Button(self.root, text="Démarrer", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.quit_button = tk.Button(self.root, text="Quitter", command=self.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=10)

    def start(self):
        # Lance le jeu
        self.game.init_game()

    def pause(self):
        # Pause le jeu
        if self.game.flag:
            self.game.flag = 0
            self.canvas.draw_bottons(self.game.promp)
        else :
            self.game.flag = 1
            self.game.run_game()
    
    def esc(self,event):
        # Pause le jeu
        if self.game.flag:
            self.game.flag = 0
            self.canvas.draw_bottons(self.game.promp)
        else :
            self.game.flag = 1
            self.game.run_game()

    def quit(self):
        """
        Boîte de dialogue du protocole de fermeture de la fenêtre principale
        """
        self.game.flag = 0
        if tk.messagebox.askokcancel("Quitter", "Quitter le logiciel ?\n"):
            self.root.destroy()
            sys.exit(0)

    def mainloop(self):
        self.root.mainloop()


