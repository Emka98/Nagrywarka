import os

class Disc:
    
    def __init__(self, node=None, size=0, name=None):
        self.node = node  
        self.size = int(size)
        self.name = name
    
    def __str__(self):
        return f"{self.name} ({self.size / (1024**3):.0f} GB)"
    
    def __repr__(self):
        return self.__str__()
    
class Distibution:
    
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()