import sys
import functools
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from form_ui import Ui_Form
from objects import Distibution
from mangment import discList
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
        self.setWindowTitle("Nagrywarka Dysków")
        
        self.ui.comboBox_disc.showPopup = discShow(self, self.ui.comboBox_disc.showPopup)
        self.ui.comboBox_distribution.showPopup = self.chooser_distribution
        self.ui.pushButton_run.clicked.connect(self.clickRun)
        

    def update_progress_progressBar_clean(self, value):
        self.ui.progressBar_clean.setValue(value)
        
    def update_progress_progressBar_record(self, value):
        self.ui.progressBar_record.setValue(value)
        
    def chooser_distribution(self):
        self.ui.comboBox_distribution.clear()
        
        file = QFileDialog.getOpenFileName(
            self,
            "Wybierz obraz do nagrania",
            "/home/",
            "Wszystkie pliki (*);;qcow2 (*.qcow2);;img (*.img)",
        )
        
        dist = Distibution(file[0])
        self.ui.comboBox_distribution.addItem(dist.name, userData=dist)
        
    def start(self):
        self.update_progress_progressBar_clean(0)
        self.update_progress_progressBar_record(0)
        
        self.ui.pushButton_run.setEnabled(False)
        self.ui.checkBox_clean.setEnabled(False)
        self.ui.checkBox_record.setEnabled(False)
        
    def stop(self):
        self.ui.pushButton_run.setEnabled(True)
        self.ui.checkBox_clean.setEnabled(True)
        self.ui.checkBox_record.setEnabled(True)
   
    def clickRun(self):
        self.start()
        
        clean = self.ui.checkBox_clean.isChecked()
        record = self.ui.checkBox_record.isChecked()
        disc = self.ui.comboBox_disc.currentData()
        distribution = self.ui.comboBox_distribution.currentData()
        
        self.worker_thread = WorkerThread(clean, record, disc, distribution)
        self.worker_thread.progressClean_updated.connect(self.update_progress_progressBar_clean)
        self.worker_thread.progressRecord_updated.connect(self.update_progress_progressBar_record)
        self.worker_thread.finished.connect(self.stop)
        self.worker_thread.start()
                
if __name__ == "__main__":
    
    if os.geteuid() != 0:
        print("Wymagane uprawnienia administratora. Uruchamianie pkexec...")
        
        env_args = []
        if "DISPLAY" in os.environ:
            env_args.append(f"DISPLAY={os.environ['DISPLAY']}")
        if "XAUTHORITY" in os.environ:
            env_args.append(f"XAUTHORITY={os.environ['XAUTHORITY']}")

        os.execvp("pkexec", ["pkexec", "env"] + env_args + [sys.executable] + sys.argv)
    
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())