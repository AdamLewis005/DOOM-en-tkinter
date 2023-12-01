from math import tan,radians,sqrt,cos


class Raycasting :
    """ rayons sont lancés Ils déterminent la distance
de l’observateur aux murs """
    angle = 330
    id = 0
    def __init__(self,x,y,width,height):
        self.width = width
        self.height = height
        self.ecart = 60/width 
        self.x = x
        self.y = y
        Raycasting.angle = (Raycasting.angle+ self.ecart)%360 #calcule l'ecart entre chaque rayon mais ca fait planter avec le % dans le canvas // problem resolu 
        self.tang = tan (radians(self.angle)) #je le met ici pour faire le calcul que une fois
        if (self.angle >= 90 and self.angle <180) or (self.angle <= 360 and self.angle >=270) :
            self.tang = -self.tang
        #print(self.tang)
        self.intersection_horizontal = Raycasting.intersection_horizontal(self)
        self.intersection_vertical = Raycasting.intersection_vertical(self)
        self.id = Raycasting.id
        Raycasting.id+=1
        self.delta = ((self.width/2) / (tan (radians(60/2))) )
        

    def intersection_vertical(self):
        """ Calcul de la première intersection verticale """
        xv =  (self.x // 5) * 5 #j'utilise 5 au lieu de 64 psq mes caree font 5 pixel sur 5 et pas 64
        
        if self.angle <= 90 or self.angle >=270:
            xv += 5
        if self.angle <= 180 and self.angle >=0: 
            yv = self.y + abs(self.x - xv)  * self.tang
        else : 
            yv = self.y - abs(self.x - xv)  * self.tang
        """
             270°               }
           |     |              }
     225°  |     |  315°        <-- dans la partie haut on soustrai a notre position car le rayon dois aller en dessous du joueur sur laxe des x
           |     |              }
180 ---------+     +--------- 0
           |     |
    135°   |     |  45°
           |     |
             90°

        
        """

        #print("v",xv,yv)
        return [xv , yv]
    
    def intersection_horizontal(self):
        """ Calcul de la première intersection  horizontale """
        yh = (self.y // 5) * 5
        if self.angle <= 180 and self.angle >=0:
            yh += 5
        if self.angle <= 90 or self.angle >=270 :
            xh = self.x  + abs(self.y - yh) / self.tang
        else :
            xh = self.x  - abs(self.y - yh) / self.tang

        """
             270°               
           |     |              
     225°  |     |  315°        
           |     |              
180 ---------+     +--------- 0
           |     |
    135°   |     |  45°
           |     |
             90°
^^^^^^^^^^^ <== dans la partie gauche on soustrai a notre position car le rayon dois aller dans les negatif par aport au joueur sur laxe des y
        
        """

        #print("h",xh,yh)
        return [xh , yh]
    
    def intersection_h_suivante(self):
        """Calcul de l'intersection  horizontale suivante"""
        #self.intersection_horizontal[1] +=  5
        # pas besoin car on le fait dans le init
        #if  (self.angle >= 90 and self.angle <=180) or (self.angle <= 360 and self.angle >=270) : # verif si on de trouve dans le 2 ou 4 eme quadrant pour mult tangente par -1
            #self.intersection_horizontal[0] +=  5 / tan(radians(self.angle))*-1
            
        #else :
        """on change que les y car +++ quand on detect le mur de gauche on passe sous le joueur et on arrive au milieu le y ne change pas
                                   + +
                                   +++
        """
        if self.angle <= 180 and self.angle >=0 :
            self.intersection_horizontal[1] +=  5
        else :
            self.intersection_horizontal[1] -=  5
        """on change que les x car +++ quand on detect le mur du bas et on arrive au milieu le y ne change pas
                                   + +
                                   +++
        """
        if self.angle <= 90 or self.angle >=270 : # meme raison que dans insertion_horizontal
            self.intersection_horizontal[0] +=  5 / self.tang
        else :
            self.intersection_horizontal[0] -=  5 / self.tang
        

    def intersection_v_suivante(self):
        """Calcul de l'intersection  verticale suivante"""
        #self.intersection_vertical[0] +=  5
        #if  (self.angle >= 90 and self.angle <=180) or (self.angle <= 360 and self.angle >=270) : # verif si on de trouve dans le 2 ou 4 eme quadrant pour mult tangente par -1
            #self.intersection_vertical[1] +=  5 * (tan(radians(self.angle))*-1)
        #else :
        if self.angle <= 90 or self.angle >=270 :
            self.intersection_vertical[0] +=  5
        else:
            self.intersection_vertical[0] -=  5

        if self.angle <= 180 and self.angle >=0 : #meme raison que interserction_v
            self.intersection_vertical[1] +=  5 * self.tang
        else :
            self.intersection_vertical[1] -=  5 * self.tang
            
        


    def wall_touched(self,map):
        """ retourn un booleen qui indique si le rayon a atient un mur a lintersection ou pas"""
        

        """"
        vide = True
        dif_vertical = abs(self.x-self.intersection_vertical[0])
        dif_horizontal = abs(self.x-self.intersection_horizontal[0])
        #print (dif_vertical,dif_horizontal)
        if dif_vertical > dif_horizontal:
            case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            if tag != 'vide': #verifier le croisement vertical aussi
                vide = False 
                 
            
            case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
                

            while tag == 'vide' and vide :
                self.intersection_h_suivante()
                case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
               
            
                if tag != 'vide': #verifier le croisement vertical aussi
                    vide = False 
                
                self.intersection_v_suivante()
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                print (tag)
        else :
            
            case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            print (tag)
            if tag != 'vide': #verifier le croisement horizontal aussi
                vide = False
                 
            print("lok",self.intersection_horizontal)
            case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)[0]
            tag = canvas.gettags(case)[0]
            

            while tag == 'vide' and vide :
                self.intersection_v_suivante()
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
            
                if tag != 'vide': #verifier le croisement horizontal aussi
                    vide = False 
                    
                
                self.intersection_h_suivante()
                case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                print (tag)
        """
        """
        #h_or_v valeur bool pour verifier si le mur est toucher horizontalement ou verticalement True pour h false pour v
        vide = True
        dif_vertical = abs(self.x-self.intersection_vertical[0])
        dif_horizontal = abs(self.x-self.intersection_horizontal[0])
        print (dif_vertical,dif_horizontal)
        if dif_vertical > dif_horizontal:
            case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            if tag != 'vide': #verifier le croisement vertical aussi
                vide = False 
                h_or_v = True  
            else :
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                h_or_v = False

            while tag == 'vide' and vide :
                self.intersection_h_suivante()
                case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
               
            
                if tag != 'vide': #verifier le croisement vertical aussi
                    vide = False 
                    h_or_v = True
                else :
                    self.intersection_v_suivante()
                    case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                    tag = canvas.gettags(case)[0]
                    h_or_v = False
                print (tag)
        else :
            
            case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            print (tag)
            if tag != 'vide': #verifier le croisement horizontal aussi
                vide = False
                h_or_v = False 
            else :
                case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                h_or_v = True

            while tag == 'vide' and vide :
                self.intersection_v_suivante()
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
            
                if tag != 'vide': #verifier le croisement horizontal aussi
                    vide = False 
                    h_or_v = False
                else :
                    self.intersection_h_suivante()
                    case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                    tag = canvas.gettags(case)[0]
                    h_or_v = True
                print (tag)
        """
        """
        vide = True
        case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)#verif croisement horrizontal
        tag = canvas.gettags(case)[0]
        if tag != 'vide': #verifier le croisement vertical aussi
            vide = False 
        if not vide :
            case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            
        
        while tag == 'vide' and vide :
            self.intersection_h_suivante()
            case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
            tag = canvas.gettags(case)[0]
            
            if tag != 'vide': #verifier le croisement vertical aussi
                vide = False 
            else :
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
            print (tag)

        
        
        if h_or_v:
            print("h")
            canvas.draw_ray_h(self)
        else:
            print("v")
            canvas.draw_ray_v(self)

        
        """
        """
        dif_vertical = abs(self.x-self.intersection_vertical[0])
        dif_horizontal = abs(self.x-self.intersection_horizontal[0])
        #print (dif_vertical,dif_horizontal)
        if dif_vertical > dif_horizontal:
            print("h")
            canvas.draw_ray_h(self)
        else:
            print("v",self.x , self.y)
            canvas.draw_ray_v(self)
        print(case)
        """
        #print(self.angle)
        #a refaire utilise find_clossest aulieu de calcule pas assez rapide et fait crash facilement
        """
        
        vide = True
        while vide :
            dif_vertical = abs(self.x-self.intersection_vertical[0])
            dif_horizontal = abs(self.x-self.intersection_horizontal[0])
            #print (dif_vertical,dif_horizontal)
            if dif_vertical > dif_horizontal:
                case = canvas.find_closest(self.intersection_horizontal[0]+canvas.offset, self.intersection_horizontal[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                #print(tag)
                #print(self.intersection_horizontal)
                if tag == 'mure': #verifier le croisement horizontal aussi     #ne detecte pas le mure a verifier pk
                    vide = False
                    x = self.intersection_horizontal[0]
                    y = self.intersection_horizontal[1]
                else :
                    self.intersection_h_suivante()
                    #print(self.intersection_horizontal)
            else :
                case = canvas.find_closest(self.intersection_vertical[0]+canvas.offset, self.intersection_vertical[1]+canvas.offset)
                tag = canvas.gettags(case)[0]
                #print(tag)
                if tag == 'mure': #verifier le croisement horizontal aussi
                    vide = False
                    x = self.intersection_vertical[0]
                    y = self.intersection_vertical[1]
                else :
                    self.intersection_v_suivante()

                


        """
        
        #print ("v",self.intersection_vertical[0],self.intersection_vertical[1])
        #print ("h",self.intersection_horizontal[0],self.intersection_horizontal[1])
        #canvas.draw_ray(self,x,y)
        #canvas.draw_point(self.intersection_vertical[0],self.intersection_vertical[1])
        #canvas.draw_point(self.intersection_horizontal[0],self.intersection_horizontal[1])
        #canvas.draw_ray(self,self.intersection_vertical[0],self.intersection_vertical[1])
        #canvas.draw_ray(self,self.intersection_horizontal[0],self.intersection_horizontal[1])
        #canvas.itemconfigure(case, fill = "green")

        """ je me suis aider du site apres pour comprendre comment faire la ddetecction avec un mure https://lodev.org/cgtutor/raycasting.html  """
        vide = True
        while vide :
            #dif_vertical = sqrt((self.x-self.intersection_vertical[0])**2 + (self.y-self.intersection_vertical[1])**2)
            #dif_horizontal = sqrt((self.x-self.intersection_horizontal[0])**2 + (self.y-self.intersection_horizontal[1])**2)
            dif_vertical = abs(self.x-self.intersection_vertical[0]) #coute moin que la distance complete et pas besoin
            dif_horizontal = abs(self.x-self.intersection_horizontal[0])
            #print (dif_vertical,dif_horizontal)
            #print(map)
            if dif_vertical < dif_horizontal:
                if self.angle <= 90 or self.angle >=270 : # on veux detecter le cote du mure le plus proche du jouer dans ce cas le cote gauche
                    case = map[int(self.intersection_vertical[1]//5)][int(self.intersection_vertical[0]//5)]#regarde dans la liste map si in est pas sur un mure , // 5 psq les case sont de 5 pixel et on veux retrouver sur un cadriage de 16x 16 et 85x85
                    if case !="0":  
                        vide = False
                        x = self.intersection_vertical[0]
                        y = self.intersection_vertical[1]
                    else:
                        self.intersection_v_suivante()
                else:#dans ce quadrant le cote droit
                    case = map[int(self.intersection_vertical[1]//5)][int(self.intersection_vertical[0]//5)-1]#regarde dans la liste map si in est pas sur un mure , // 5 psq les case sont de 5 pixel et on veux retrouver sur un cadriage de 16x 16 et 85x85
                    if case!="0":  
                        vide = False
                        x = self.intersection_vertical[0]
                        y = self.intersection_vertical[1]
                    else:
                        self.intersection_v_suivante()
            else:
                if self.angle <= 180 and self.angle >=0 :# on veux detecter le cote du mure le plus proche du jouer dans ce cas le cote haut
                    case = map[int(self.intersection_horizontal[1]//5)][int(self.intersection_horizontal[0]//5)]#x et y inverse a la liste map
                    if case!= '0': 
                        vide = False
                        x = self.intersection_horizontal[0]
                        y = self.intersection_horizontal[1]
                    else:
                        self.intersection_h_suivante()
                else:# dans ce cas le cote bas
                    case = map[int(self.intersection_horizontal[1]//5)-1][int(self.intersection_horizontal[0]//5)]
                    if case!= '0': #x et y inverse a la liste map
                        vide = False
                        x = self.intersection_horizontal[0]
                        y = self.intersection_horizontal[1]
                    else:
                        self.intersection_h_suivante()

        #print(self.angle)
        #print ("v",self.intersection_vertical[0],self.intersection_vertical[1])
        #print ("h",self.intersection_horizontal[0],self.intersection_horizontal[1])
        #print("co",x,y)
        
        #canvas.draw_ray(self,x,y)
        return x,y, case
    
    def walls(self,canvas,x,y,case):
        
        d = sqrt((self.x-x)**2 + (self.y-y)**2) #pour rendre le mure une taill reel
        
        if self.id >= self.width/2 :
            r = (10 *(self.delta/ d))/cos(radians(self.ecart*(self.id%400)))#langle entre le rayon du milieu et celui actuel
        else:
            r = (10 *(self.delta/ d))/cos(radians(self.ecart*(400-self.id)))  # o = n , 1 = n-1, 2 = n-2 ...
        canvas.draw_wall(self,r,x,y,int(case))

     
        

#teste
"""
R = Raycasting(12.5,12.5,320)   
print(R.intersection_vertical)
print(R.intersection_horizontal)
Raycasting.intersection_h_suivante(R)
Raycasting.intersection_v_suivante(R)
print(R.intersection_horizontal)
print(R.intersection_vertical)
Raycasting.intersection_h_suivante(R)
Raycasting.intersection_v_suivante(R)
print(R.intersection_horizontal)
print(R.intersection_vertical)
"""