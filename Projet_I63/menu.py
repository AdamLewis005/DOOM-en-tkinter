import tkinter as tk
from map import Map

class Menu:
    """ bouton menu """
    def __init__(self, parent,game):
        self.parent = parent
        self.game=game
        self.menu_bar = tk.Menu(parent)
        parent.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Importer une map",accelerator="CTRL+O", command=lambda:self.open())
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=self.quit)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_name = "map.map"

    def open(self):
        # Ouvre un monde existant
        self.file_name = tk.filedialog.askopenfilename(title="Importer un monde")
        self.game.change_map(self.file_name)


    def quit(self):
        """
        Boîte de dialogue du protocole de fermeture de la fenêtre principale
        """
        if tk.messagebox.askokcancel("Quitter", "Quitter le logiciel ?\n"):
            self.parent.destroy()
            sys.exit(0)
