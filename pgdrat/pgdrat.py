class person:
    def __init__(self,fname,lname,age):
        self.__fname = fname
        self.__lname = lname
        self.__age   = age
    
    # getter & setter
    
    def getfname(self):
        return self.__fname
    
    def setfname(self, newfname):
        self.__fname = newfname
    
    def getlname(self):
        return self.__lname
    
    def setlname(self, newlname):
        self.__lname = newlname
    
    def getage(self):
        return self.__age
    
    def setage(self, newage):
        self.__age = newage