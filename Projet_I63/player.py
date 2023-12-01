class Player:
    """Joueur"""
    id = 0
    def __init__(self,x,y,color):
        Player.id += 1
        self.x = x
        self.y = y
        self.angle = 60
        self.color = color

    

    
