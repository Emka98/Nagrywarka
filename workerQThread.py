from PySide6.QtCore import QThread, Signal
from objects import Disc, Distibution
from mangment import cleanDisc, recordDisc

class WorkerThread(QThread):
    
    progressClean_updated = Signal(float)
    progressRecord_updated = Signal(float)

    def __init__(self, clean:bool, record:bool, disc:Disc, distribution:Distibution = None):
        
        super().__init__()
        self.clean = clean
        self.record = record
        self.disc = disc
        self.distribution = distribution
        
    def run(self):
            try:
                if self.clean:
                    for i in cleanDisc(self.disc):
                        print(i)
                        self.progressClean_updated.emit(i)

                if self.record:
                    for i in recordDisc(self.disc, self.distribution):
                        print(i)
                        self.progressRecord_updated.emit(i)

            except Exception as e:
                print(f"Błąd podczas wykonywania zadania w wątku: {e}")
                return

            return
