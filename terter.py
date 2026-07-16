import sys
from PyQt6.QtCore import QThread, pyqtSignal
import time
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel
from objects import Disc

class WorkerThread(QThread):

    progressClean_updated = pyqtSignal(float)
    progressRecord_updated = pyqtSignal(float)
    
    def __init__(self, action: str):
        super().__init__()
        self.action = action
    
    def run(self):
        if self.action == "clean":
            for i in range(101):
                time.sleep(0.1)
                self.progressClean_updated.emit(i)
        if self.action == "record":
            for i in range(101):
                time.sleep(0.1)
                self.progressRecord_updated.emit(i)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QThread Example")
        self.setFixedSize(300,200)

        vbox = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_thread)

        vbox.addWidget(self.button)

        self.progress_label = QLabel("Progress : ")
        vbox.addWidget(self.progress_label)

        self.setLayout(vbox)

        self.worker_thread = WorkerThread("record")
        self.worker_thread.progressRecord_updated.connect(self.update_progress)
        
    def start_thread(self):
        self.button.setEnabled(False)
        self.worker_thread.start()


    def update_progress(self, value):
        self.progress_label.setText(f"Progress clean : {value}%")
        if value == 100:
            self.button.setEnabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



