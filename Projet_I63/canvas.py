import tkinter as tk
from map import Map
from raycasting import Raycasting

class Canvas(tk.Canvas):
    offset = 10  # pour que la map soit pas coupe/coller a la bordure du canvas
    map = None
    def __init__(self,game, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.player = []
        self.game = game
        self.ray = Raycasting.angle
        self.width =kwargs["width"]
        self.height=kwargs["height"]
        self.texture = [[],["gray","green","green","green","gray"],["#523A28"],["black","red","black","black","black","black","black","black"]] # primier [] > type de mure deuxieme [] > texture du mure
         
        

    def draw_map(self):
        #dessine la carte en haut a droite 85 * 85 pixel
        
        x = 0
        y = 0
        
        for ligne in self.map :
            for case in ligne:
                if case != '0':
                    self.create_rectangle(x+self.offset,y+self.offset,x+5+self.offset,y+5+self.offset,fill = 'black',tags = "mure",width=0)
                else:
                    self.create_rectangle(x+self.offset,y+self.offset,x+5+self.offset,y+5+self.offset,fill = 'white',tags = "vide",width=0)
                x = (x + 5)%85 
            y +=5

    def draw_player(self,player):#dessine le joueur
        
        p = self.create_rectangle(player.x+self.offset,player.y+self.offset,player.x+2+self.offset,player.y+2+self.offset,fill = player.color,tags = "player",width=0)
        self.player= [player,p] 
        

    def draw_ray_h(self,ray):#dessine le rayon qui trouche un mure horizzontal
        self.create_line(ray.x+self.offset,ray.y+self.offset,ray.intersection_horizontal[0]+self.offset,ray.intersection_horizontal[1]+self.offset,fill="pink")

    def draw_ray_v(self,ray):#dessine le rayon qui trouche un mure vertical
        self.create_line(ray.x+self.offset,ray.y+self.offset,ray.intersection_vertical[0]+self.offset,ray.intersection_vertical[1]+self.offset,fill="pink")

    def draw_ray(self,ray,x,y):
        self.create_line(ray.x+self.offset,ray.y+self.offset,x+self.offset,y+self.offset,fill = "pink",tag="ray") 

    def delete_ray(self):
        idr = self.find_withtag("ray")
        idr += self.find_withtag("wall")
        idr += self.find_withtag("gun")
        Raycasting.angle = self.ray
        Raycasting.id = 0
        for id in idr :
            self.delete(id)  

    def move_player_left(self,event):
        angle = (self.ray+30)%360
        if 225<angle<315: # se deplace la ou le joueur regarde
            if self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "0": #colision
                self.player[0].x -= 1
                self.move(self.player[1],-1, 0)
        elif 45<angle<135:
            if self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "0":
                self.player[0].x += 1
                self.move(self.player[1],1, 0)
        elif 135<angle<225:
            if self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y += 1
                self.move(self.player[1],0, +1) 
        else:
            if self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y -= 1
                self.move(self.player[1],0, -1)

            

    def move_player_up(self,event):
        angle = (self.ray+30)%360
        # se deplace la ou le joueur regarde 
        if 225<angle<315: # up
            if self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y -= 1
                self.move(self.player[1],0, -1)
        elif 45<angle<135: # down
            if self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y += 1
                self.move(self.player[1],0, +1) 
        elif 135<angle<225: #left
            if self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "0": #colision
                self.player[0].x -= 1
                self.move(self.player[1],-1, 0)
        else: #right
            if self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "0":
                self.player[0].x += 1
                self.move(self.player[1],1, 0)
       

    def move_player_down(self,event):
        angle = (self.ray+30)%360
        if 225<angle<315: #down
            if self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y += 1
                self.move(self.player[1],0, +1)
        elif 45<angle<135: # up
            if self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y -= 1
                self.move(self.player[1],0, -1)
        elif 135<angle<225:
            if self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "0":
                self.player[0].x += 1
                self.move(self.player[1],1, 0)
        else:
            if self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "0": #colision
                self.player[0].x -= 1
                self.move(self.player[1],-1, 0)

    def move_player_right(self,event):
        angle = (self.ray+30)%360
        if 225<angle<315: #right
            if self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x+1)//5)] == "0":
                self.player[0].x += 1
                self.move(self.player[1],1, 0)
        elif 45<angle<135:
            if self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "2":
                self.game.next_map()
            elif self.map[int(self.player[0].y//5)][int((self.player[0].x-1)//5)] == "0": #colision
                self.player[0].x -= 1
                self.move(self.player[1],-1, 0)
        elif 135<angle<225:
            if self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y-1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y -= 1
                self.move(self.player[1],0, -1)
        else:
            if self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "2":
                self.game.next_map()
            elif self.map[int((self.player[0].y+1)//5)][int(self.player[0].x//5)] == "0":
                self.player[0].y += 1
                self.move(self.player[1],0, +1) 

        


    def rotate_player_right(self,event):
        Raycasting.angle =  (self.ray+10 )%360
        self.ray += 10

    def rotate_player_left(self,event):
        Raycasting.angle =  (self.ray-10 )%360
        self.ray -= 10
        

    def draw_point(self,x,y):
        self.create_oval(x+self.offset,y+self.offset,x+self.offset+3,y+self.offset+3,fill = "red",tag="ray")
    
    def draw_back(self):
        """ dessine le ciel et le sol """
        self.create_rectangle(0,0,self.width,self.height/2,fill="lightblue")
        self.create_rectangle(0,self.height/2,self.width,self.height,fill="#B68D40")
    
    def draw_wall(self,ray,r,x,y,case):
        start = -r/2 + self.height/2 
        end = r/2 + self.height/2
        if (ray.angle>=225 and ray.angle<=315) or (ray.angle>=45 and ray.angle<=135):
            
            self.create_line(ray.id,start,ray.id,end,fill=self.texture[case][int(x%len(self.texture[case]))],tag="wall") # texture proleme 
            self.create_line(ray.id,start,ray.id,start-1,fill="black",tag="wall")
            self.create_line(ray.id,end,ray.id,end+1,fill="black",tag="wall")
        else:
            self.create_line(ray.id,start,ray.id,end,fill=self.texture[case][int(y%len(self.texture[case]))],tag="wall")
            self.create_line(ray.id,start,ray.id,start-1,fill="black",tag="wall")
            self.create_line(ray.id,end,ray.id,end+1,fill="black",tag="wall")
    
    def draw_bottons(self,img):     
        self.create_image(150,150, anchor=tk.NW, image=img,tag="wall") 
        self.create_text(400,100,text = "FIND THE DOOR",font= ("",30,"bold"),tag="wall")

    def fin(self,time,win):
        self.create_image(0,0, anchor=tk.NW, image=win,tag="wall")
        #self.create_text(400,100,text = "FIN",font= ("",30,"bold"),tag="wall")
        self.create_text(400,500,text = "time : "+str(int(time-self.game.start))+" seconde",fill="white",font= ("",30,"bold"),tag="wall")
        self.game.flag = 0
        print("win")

    def draw_gun(self):
        for i in range (100):
            self.create_line(460+i//2,450,650+i,600,tag="gun",fill="#31352E")
            self.create_line(460,450+i//2,650,600+i,tag="gun",fill="#C1BCB8")

        for i in range(100):
            self.create_line(460+i//2,450,485,430,tag="gun",fill= "#31352E")