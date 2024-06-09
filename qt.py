import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.resize(300, 300)
        self.setWindowIcon(QIcon('img/logo.ico'))
        
        layout = QVBoxLayout(self)
        
        self.label = QLabel("Drop the STEP files here", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        from s2s import s2s #import here to load the window faster at app start
        s2s(files)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()    
    sys.exit(app.exec_())
