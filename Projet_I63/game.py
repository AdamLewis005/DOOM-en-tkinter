from map import Map
from canvas import Canvas
from raycasting import Raycasting
import time

class Game :
    """ jeu """
    canvas = None
    def __init__(self,player):
        self.maplist= ["map.map","map1.map",]#"map2.map","map3.map"]
        self.map = Map("map.map")
        self.nbmap = 0
        self.player = player
        self.status_bar = None
        self.promp = None
        self.win = None
        self.flag= 0
        self.frame = 0
        self.start = 0
        self.last = 0
        
        
        


    def init_game(self):
        self.start = time.time()
        self.nbmap = 0
        self.last = self.start
        self.canvas.draw_back()
        self.run_raycasting()
        Canvas.map = self.map.liste
        self.canvas.draw_map()
        self.canvas.draw_player(self.player)
        self.canvas.draw_bottons(self.promp)
        self.run_game()
        
    def run_game(self):
        self.flag = 1
        self.canvas.delete_ray()
        self.status_bar.update(int(self.player.x),int(self.player.y),Raycasting.angle+30,self.fps())
        self.run_raycasting()
        if self.frame <= 25:
            self.canvas.draw_bottons(self.promp)
        self.canvas.draw_gun()
        self.canvas.after(self.frame,self.loop)

    def loop(self):
        if self.flag:
            self.run_game()

            
        
    def fps(self):
        self.frame += 1
        time_drawing = time.time() - self.last
        fps = self.frame / time_drawing
        return int(fps)

    def next_map(self):
        """reinitialise tout a 0 et charge la prochaine map"""
        self.canvas.ray = 330
        self.canvas.delete_ray()
        self.player.x = 7.1
        self.player.y = 7.1
        self.nbmap += 1
        if self.nbmap < len(self.maplist):
            self.map = Map(self.maplist[self.nbmap]) # update la detection des mure par les rayon
            Canvas.map = self.map.liste # update les colision 
            
        else :
            self.canvas.fin(time.time(),self.win)

    def change_map(self,file):
        self.canvas.ray = 330
        self.canvas.delete_ray()
        self.player.x = 7.1
        self.player.y = 7.1
        self.map = Map(file)
        Canvas.map = self.map.liste
        


    def run_raycasting(self):
        R = Raycasting(self.player.x,self.player.y,self.canvas.width,self.canvas.height)
        l = R.wall_touched(self.map.liste)
        self.canvas.draw_ray(R,l[0],l[1])
        R.walls(self.canvas,l[0],l[1],l[2])
        for i in range(self.canvas.width-2):
            R = Raycasting(self.player.x,self.player.y,self.canvas.width,self.canvas.height)
            l = R.wall_touched(self.map.liste)
            R.walls(self.canvas,l[0],l[1],l[2])
        R = Raycasting(self.player.x,self.player.y,self.canvas.width,self.canvas.height)
        l = R.wall_touched(self.map.liste)
        R.walls(self.canvas,l[0],l[1],l[2])
        self.canvas.draw_ray(R,l[0],l[1])



        