class Nodo:
    __per = object
    __sig = object
    def __init__(self, persona):
        self.__per = persona
        self.__sig = None
    def setPer(self, persona):
        self.__per = persona
    def setSig(self, siguiente):
        self.__sig = siguiente
    def getPer(self):
        return self.__per
    def getSig(self):
        return self.__sig