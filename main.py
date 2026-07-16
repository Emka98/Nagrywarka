import sys
import functools

from PySide6.QtWidgets import QApplication, QWidget 
from form_ui import Ui_Form
from objects import Disc, Distibution
from mangment import discList, cleanDisc, recordDisc, formatToMSDOS
from workerQThread import WorkerThread

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
        self.ui.pushButton_run.clicked.connect(self.clickRun)
       
        
        
    def update_progress_progressBar_clean(self, value):
        self.ui.progressBar_clean.setValue(value)
   
    def clickRun(self):
        if self.ui.checkBox_clean.isChecked():
            self.ui.pushButton_run.setEnabled(True)
            self.worker_thread = WorkerThread("record")
            self.worker_thread.progressRecord_updated.connect(self.update_progress_progressBar_clean)
            self.worker_thread.start()
            self.ui.pushButton_run.setEnabled(False)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())