from PySide2 import QtWidgets
from PySide2.QtWidgets import QVBoxLayout


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets()
        self.setup_connections()

    def create_widgets(self):
        self.btn_clique = QtWidgets.QPushButton("Clique")

    def modify_widgets(self):
        pass

    def create_layout(self):
        self.main_layout = QVBoxLayout(self)

    def add_widgets(self):
        self.main_layout.addWidget(self.btn_clique)

    def setup_connections(self):
        self.btn_clique.clicked.connect(self.bouton_clicked)

    def bouton_clicked(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("Bravo")
        message_box.setText("Tu as reussi ta premiere application!")
        message_box.exec_()