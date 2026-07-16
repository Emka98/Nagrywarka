import sys
import functools

from PySide6.QtWidgets import QApplication, QWidget 
from form_ui import Ui_Form
from workerQThread import Worker
from mangment import discList, cleanDisc, recordDisc, formatToMSDOS

def discShow(self, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self.ui.comboBox_disc.clear() 
        for disc in discList():
            self.ui.comboBox_disc.addItem(str(disc), disc)
        return func(*args, **kwargs)
    return wrapper
        
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox_disc.showPopup = discShow(self, self.ui.comboBox_disc.showPopup)
    
    def clearOnlyDisc():
        pass
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())