import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.create_main_layout()

    def create_main_layout(self):
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.text_label = QLabel("Please enter your name")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.text_label)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.submit_button.clicked.connect(self.display_text)

    def display_text(self):
        name = self.text_box.text()
        self.text_label.setText("Hello {0}".format(name))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
