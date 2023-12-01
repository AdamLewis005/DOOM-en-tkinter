
class Map:
    """ creation de la class map qui represente la carte """
    def __init__(self,file_name):
        self.name = file_name
        self.liste =self.open_map() #initialise des que la map est cree

    def open_map(self):
        #ouvre le fichier et met la map sous forme de liste de string
        file = open(self.name,"r")
        liste= []
        for ligne in file :
            liste += [ligne.strip()]
        return liste
