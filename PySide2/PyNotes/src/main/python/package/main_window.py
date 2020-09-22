from PySide2 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyNotes")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets()
        self.setup_connections()

    def create_widgets(self):
        pass

    def modify_widgets(self):
        pass

    def create_layout(self):
        pass

    def add_widgets(self):
        pass

    def setup_connections(self):
        pass

