class Pays:
    def __init__(self, nom, competences,img):
        self.nom = nom #string
        self.competences = competences #dictionnaire
        self.img = img
    #définit le multiplier pour une compétence
    def setMultiplier(self, competence, multiplier):
        #si la compétence existe
        if self.competences.has_key(competence):
            #on change son multiplier
            self.competences[competence] = multiplier
        else:
            return
