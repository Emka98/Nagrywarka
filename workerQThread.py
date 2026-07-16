from PySide6.QtCore import QThread, Signal

class Worker(QThread):

    def __init__(self, funkcja, progresbar):
        super().__init__()
        self.funkcja = funkcja
        self.progresbar = progresbar