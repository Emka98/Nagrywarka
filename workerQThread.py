from PyQt6.QtCore import QThread, pyqtSignal
from objects import Disc, Distibution
import time
from mangment import cleanDisc, recordDisc

class WorkerThread(QThread):
    
    progressClean_updated = pyqtSignal(float)
    progressRecord_updated = pyqtSignal(float)

    # def __init__(self, action_type: str, disc: Disc, distribution: Distibution = None):
    def __init__(self, action: str):
        super().__init__()
        self.action = action
        # self.disc = disc
        # self.distribution = distribution
        
    def run(self):
        if self.action == "clean":
            for i in range(101):
                time.sleep(0.1)
                self.progressClean_updated.emit(i)
        elif self.action == "record":
            for i in range(101):
                time.sleep(0.1)
                self.progressRecord_updated.emit(i)
