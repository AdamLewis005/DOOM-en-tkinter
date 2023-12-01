import tkinter as tk
class StatusBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.player_positionx_label = tk.Label(self, text="Jouer coods x : 0")
        self.player_positionx_label.pack(side=tk.LEFT)
        self.player_positiony_label = tk.Label(self, text="y : 0")
        self.player_positiony_label.pack(side=tk.LEFT)
        self.player_direction_label = tk.Label(self, text="angle : 0")
        self.player_direction_label.pack(side=tk.LEFT)
        self.FPS_label = tk.Label(self, text="FPS : 0")
        self.FPS_label.pack(side=tk.LEFT)

    def update(self, x,y ,angle,fps):
        self.player_positionx_label.config(text="Jouer coods : {}".format(x))
        self.player_positiony_label.config(text="y : {}".format(y))
        self.player_direction_label.config(text="angle : {}".format(angle%360))
        self.FPS_label.config(text= "FPS : {}".format(fps))

